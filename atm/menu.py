#!/usr/bin/env python
import sys
from withdaw import withdaw
from cashin import cashin
from checkbill import checkbill
from shop import shop
#user = 'xielan'
#time = 2015
#left = 15000
def menu_select(user,left):
    act_num = raw_input('plz input your select(1 2 3 4 5):').strip()
    while len(act_num) == 0:
	break
    if act_num == '1':
        left = withdaw(user,left)
    elif act_num == '2':
        left = cashin(user,left)
	print type(left)
    elif act_num == '3':
        checkbill(user)
    elif act_num == '4':
        left = shop(user,left)
    elif act_num == '5':
        exit()
    else:
         print 'no this select'
    return left
    print left
#while True:
def menu_show(user,left):
    print '''    list
\t1.withdaw \t2.cashin \t 3.checkbilli \t 4.shop \t 5.quit'''
#    print user
    left = menu_select(user,left)
    return left
 #   print type(left)
