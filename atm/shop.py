#!/usr/bin/env python
from logging import logbill
def shop(user,left):
    shoplist = file('H:\\python\\atm\\shoplist')
    shop_dic = {}
    time = 2015
    print '\t\tshoplist',
    for line in shoplist.readlines():
        new_line = line.split()
        print '''
    \t%s\t\t|%d
        ''' % (new_line[0],int(new_line[1])),
        shop_dic[new_line[0]] = int(new_line[1])
    while True:
        if left >= int(min(shop_dic.values())):
            want = raw_input('plz input you want buy:')
  	    if want == 'q' or want == 'quit':
		break
            while shop_dic.has_key(want):
                want_price = int(shop_dic.get(want))
		if want_price >= left:
		    print 'your cant buy this,another'
   		    break
		else:
                    acttion = 'shop %s' %want
    	            left = left - want_price
                    logbill(user,time,acttion,want_price,left)
                    break
            else:
    	        print 'not this in list'
        else:
    	    print 'no enough money'
    	    break
    return left
