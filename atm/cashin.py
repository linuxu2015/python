#!/usr/bin/env python
from logging import logbill
def cashin(user,left):
    #user = 'xielan'
    time = 2015
    acttion = 'cashin\t'
    #left = 15000
    cashin_num = int(raw_input('plz input the num you want cashin:'))
    left = left + cashin_num
    log_num = '+%s' % cashin_num
    logbill(user,time,acttion,log_num,left)
    return left
