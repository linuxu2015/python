# -*- coding: cp936 -*-
'关键字搜索'
while True:
    condition = raw_input('plz input your condition:')
    format_c = condition.strip()
    listfile = file('namelist.txt')
    result = False
    while True:
        namelist = listfile.readline()
        if namelist == '':
            break
        while format_c in namelist:
            print namelist
            result = True
            break
    if result == False:
        print 'no match about %s' % format_c
