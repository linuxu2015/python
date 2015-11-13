#!/usr/bin/env python
import docker
import list_container
from prettytable import PrettyTable
import time
global c
c = docker.Client(base_url='tcp://192.168.22.145:4243')
def listimages():
    list_image = c.images()
    l_index = len(list_image)
    for i in range(0,l_index):
        print list_image[i]['RepoTags'][0]
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
        #con_created = time.strftime('%Y-%m-%d-%H:%M:%S',111111111)
        con_hostconfig = con['HostConfig']['NetworkMode']
        con_id = con['Id']
        con_image = con['Image']
        con_labels = con['Labels']
        con_names = con['Names']
        con_ports = con['Ports']
        con_status = con['Status']
#        print '%s\t%s\t%s\t\t%s\t%s\t'%(con_command,con_created,con_hostconfig,str(con_id)[0:11],con_image)
        t.add_row([con_command,con_created,con_hostconfig,str(con_id)[0:11],con_image,con_labels,con_names,con_ports,con_status)]
    print t
listimages()
listcontainer()
