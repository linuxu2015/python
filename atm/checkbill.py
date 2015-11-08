#!/usr/bin/env python
def checkbill(user):
    billfile = file('/opt/python/bill.log')
    for line in billfile.readlines():
        if user in line:
            print line,
