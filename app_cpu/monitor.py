#!/usr/bin/env python
import time
import MySQLdb as mysql
db = mysql.connect(user='root',passwd='1qaz2wsx',db='python',host='192.168.70.193')
db.autocommit(True)
cur = db.cursor()
def getMem():
    with open('/proc/meminfo') as f:
#	print f.readline()
##	print f.readline()
#	print f.readline()
#	print f.readline()
#	print f.readline()
        total = int(f.readline().split()[1])
	free = int(f.readline().split()[1])
	f.readline()
        buffers = int(f.readline().split()[1])
        cache = int(f.readline().split()[1])
    mem_use = total - free - buffers - cache
    t = int(time.time())
    sql = 'insert into memory (memory,time) value (%s,%s)'%(mem_use/1024,t)
    cur.execute(sql)
#    print mem_use/1024,'M'
while True:
    time.sleep(2)
    getMem()
