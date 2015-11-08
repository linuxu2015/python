#!/usr/bin/env python
#user = 1
#atime =2 
#acttion =3
#cost = 4
#left = 5
#intrest = 6
def logbill(user,atime,acttion,cost,left,intrest=0):
    logfile = open('H:\\python\\atm\\bill.log','a')
    logfile.write('%s\t|%d\t|%s\t|%s\t|%d\t|%d\n' % (user,atime,acttion,cost,left,intrest))

