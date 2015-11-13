#!/usr/bin/env python
import docker
import list_container
from prettytable import PrettyTable
import time
import sys
global c
c = docker.Client(base_url='tcp://192.168.22.145:4243')
def listimages():
    image = c.images()
    l_index = len(image)
    a = PrettyTable(['creattime','labels','v_size','p_id','name','repodigests','id','size'])
    a.align['creattime'] = 'l'
    a.padding_width = 1
    for i in range(0,l_index):
        #print list_image[i]['RepoTags'][0]
        ima = image[i]
        ima_created = ima['Created']
        ima_labels = ima['Labels']
        vsize = int(ima['VirtualSize'])/1024/1024
        ima_vsize = '%d M' % vsize
        ima_pid = ima['ParentId'][0:11]
        ima_name = ima['RepoTags'][1]
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
    if len(sys.argv) != 4:
        print 'useage'
    else:
        c_id = c.create_container(image='%s' % sys.argv[1],command='%s' % sys.argv[2],name='%s' % sys.argv[3],hostname='%s' % sys.argv[3],tty=True,network_disabled=True)
        print c_id[u'Id']
        c.start(c_id[u'Id'])
listimages()
CreateContainer()
listcontainer()
