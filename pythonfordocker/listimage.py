#!/usr/bin/env python
import docker
import list_container
from prettytable import PrettyTable
import time
import sys
#import tab
global c
#c = docker.Client(base_url='tcp://192.168.1.118:4243')
c = docker.Client(base_url='tcp://127.0.0.1:4243')
def listimages():
    image = c.images()
    l_index = len(image)
    a = PrettyTable(['creattime','labels','v_size','p_id','name','repodigests','id','size'])
    a.align['creattime'] = 'l'
    a.padding_width = 1
    for i in range(0,l_index):
        #print list_image[i]['RepoTags'][0]
        ima = image[i]
        createtime = ima['Created']
        ima_created = time.strftime('%Y-%m-%d-%X',time.localtime(createtime)) 
        ima_labels = ima['Labels']
        vsize = int(ima['VirtualSize'])/1024/1024
        ima_vsize = '%d M' % vsize
        ima_pid = ima['ParentId'][0:11]
        ima_name = ima['RepoTags'][0]
        ima_digest = ima['RepoDigests']
        ima_id = ima['Id'][0:11]
        ima_size = ima['Size']
        a.add_row([ima_created,ima_labels,ima_vsize,ima_pid,ima_name,ima_digest,ima_id,ima_size])
    print a


def listcontainer():
    container = c.containers()
    t = PrettyTable(['command','creattime','hostconfig','id','image','labels','name','ports','status'])
    #t = PrettyTable(['command','creattime','hostconfig','id','image'])
    t.align['command'] = 'l'
    t.padding_width = 1
    
    #print 'command\tcreated\thostconfig     \tid    \timage    \tlabels     \tname     \tports    \tstatus'
    for i in range(0,len(container)):
        con = container[i]
        con_command = con['Command']
        #con_created = time.strftime('%Y-%m-%d-%H:%M:%S',con['Created'])
        con_created = con['Created']
        con_created = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(con['Created']))
        #con_created = time.strftime('%Y-%m-%d-%H:%M:%S',111111111)
        con_hostconfig = con['HostConfig']['NetworkMode']
        con_id = con['Id']
        con_image = con['Image']
        con_labels = con['Labels']
        con_names = con['Names'][0].strip('/')
        con_ports = con['Ports']
        con_status = con['Status']
#        print '%s\t%s\t%s\t\t%s\t%s\t'%(con_command,con_created,con_hostconfig,str(con_id)[0:11],con_image)
        t.add_row([con_command,con_created,con_hostconfig,str(con_id)[0:11],con_image,con_labels,con_names,con_ports,con_status])
    print t
#listimages()
#listcontainer()


def CreateContainer():
    try:
        image_name = raw_input('plz input your want use image name:')
        container_name = raw_input('plz input container name:')
        c_id = c.create_container(image=image_name,name=container_name,hostname=container_name,tty=True,network_disabled=True)
    #c_id = c.create_container(image='%s' % sys.argv[1],command='%s' % sys.argv[2],name='%s' % sys.argv[3],hostname='%s' % sys.argv[3],tty=True,network_disabled=True)
        c.start(c_id[u'Id'])
    except Exception:docker.errors.APIError
    print '\033[0;31;30mcan not execute your input '
#listimages()
#CreateContainer()
#listcontainer()


def StopContainer():
    stop_id = raw_input("plz input you want stop container's id:")
    c.stop(stop_id)


def SearchImage():
    searchimagename = raw_input('plz input your want search image name:')
    search_result = c.search(searchimagename)
    s_index = len(search_result)
    a = PrettyTable(['name','is_automated','is_official','is_trusted','description','star_count'])
    a.align['description'] = 'l'
    a.padding_width = 1
    for i in range(0,s_index):
        #print list_image[i]['RepoTags'][0]
        search_r = search_result[i]
        image_des = search_r['description'][0:20]
        image_auto = search_r['is_automated']
        image_office = search_r['is_official']
        image_trust = search_r['is_trusted']
        image_name = search_r['name']
        image_star = search_r['star_count']
        a.add_row([image_name,image_auto,image_office,image_trust,image_des,image_star])
    print a
#SearchImage()

   

while True:
    print '''this is the list help you to manage your docker
    1. list images
    2. list container
    3. start container
    4. stop container
    5. search images'''
    choice = raw_input('plz input your choice:')
    if choice == '1':
        listimages()
    elif choice == '2':
        listcontainer()
    elif choice == '3':
        CreateContainer()
    elif choice == '4':
        StopContainer()
    elif choice == '5':
        SearchImage()
    else:
        choice == 'q' or choice == 'quit'
        sys.exit()
