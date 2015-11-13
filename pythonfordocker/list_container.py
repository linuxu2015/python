#!/usr/bin/env python
#print c.images()
def listcontainer():
    container = c.containers()
    print 'command created hostconfig id image labels name ports status'
    for i in range(0,len(container)):
    #print container[i]['Names'][0].strip('/')
    #for j in ['Command','Created','HostConfig','Id','Image','Labels','Names','Ports','Status']:
    #    print container[i][j],
        con = container[i]
        con_command = con['Command']
        con_created = con['Created']
        con_hostconfig = con['HostConfig']['NetworkMode']
        con_id = con['Id']
        con_image = con['Image']
        con_labels = con['Labels']
        con_names = con['Names']
        con_ports = con['Ports']
        con_status = con['Status']
        print con_command,con_created,con_hostconfig,con_id,con_image
    #print con_command,con_created
    #print c.version()
