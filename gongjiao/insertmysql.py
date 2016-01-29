#!/usr/bin/env python
import MySQLdb as mysql
db = mysql.connect(user='root',passwd='1qaz2wsx',db='python',host='192.168.70.193',use_unicode = True,charset='utf8')
db.autocommit(True)
cur = db.cursor()
def insert(licence,longitude,latitude,ID,station,line,t):
	sql = "insert into gongjiao (licence,longitude,latitude,ID,station,line,time) value ('%s','%s','%s','%s','%s','%s','%s')"%(licence,longitude,latitude,ID,station,line,t)
	cur.execute(sql)
#insert('d','s',3,4,5,6)
