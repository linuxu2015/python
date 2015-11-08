#!/usr/bin/env python
from logging import logbill
#user = 'xielan'
#left = 15000
time = 2015
acttion = 'withdaw'
def withdaw(user,left):
    withdaw_num = int(raw_input('plz input you want withdaw:'))
    if withdaw_num * 1.05  <= left:
    	intrest = withdaw_num * 0.05
    	left = left - withdaw_num - intrest
        log_num = '-%s' % withdaw_num
    	logbill(user,time,acttion,log_num,left,intrest)
	print type(left)
	return left
    else:
    	print 'you have not enough money'
	return left
