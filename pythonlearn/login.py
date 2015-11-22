# -*- coding: cp936 -*-
##登录
import filetodic
filetodic.filetodic1('name_dic', 'namelist.txt')
#print name_dic
while True:
    username = raw_input('plz input your name:')
    if name_dic.has_key(username):
        while True:
            password = raw_input('plz input your password:')
            if password == name_dic.get(username):
                print 'welcome to my system'
                break
        
