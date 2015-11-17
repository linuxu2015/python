# _*_ coding=utf-8 _*_
'''
Created on 2015年11月15日

@author: Administrator
'''
import docker
#import list_container
from prettytable import PrettyTable
import time
import sys
import PT
from conf import c
def listimages():
    
    image = c.images()
    l_index = len(image)
    a = PrettyTable(['creattime','labels','v_size','p_id','name','repodigests','id','size'])
    a.align['creattime'] = 'l'
    a.padding_width = 1
    #tou = ['creattime','labels','v_size','p_id','name','repodigests','id','size']
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
    #a = PT.pt(createtime,ima_labels,ima_vsize,ima_pid,ima_name,ima_digest,ima_id,ima_size)
    print a