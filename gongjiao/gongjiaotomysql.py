#!/usr/bin/env python 
# coding:utf-8
import requests
import json
import weixin
import time
import sys
import math
from insertmysql import insert
reload(sys)
from baiduxyz import getbaiduxyz
ISOTIMEFORMAT = '%Y-%m-%d %X'
sys.setdefaultencoding('utf-8')
ISOTIMEFORMAT = '%Y-%m-%d %X'
session=requests.session() 
session.headers={
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding':'gzip, deflate',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'Cache-Control':'max-age=0',
		'Content-Length':'49',
		'Content-Type':'application/x-www-form-urlencoded',
		'Host':'ytbus.jiaodong.cn:4990',
		'Origin':'http://ytbus.jiaodong.cn:4990',
		'Proxy-Connection':'keep-alive',
		'Referer':'http://ytbus.jiaodong.cn:4990/BusPosition.asmx?op=GetBusLineStatus',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
		}
def circle(a,b):
	lat_b= 37.466839
	lng_b = 121.444287
	pk = 180 / math.pi 
	a1 = b / pk  
	a2 = a / pk  
	b1 = lat_b / pk  
	b2 = lng_b / pk  
	t1 = math.cos(a1) * math.cos(a2) * math.cos(b1) * math.cos(b2)  
	t2 = math.cos(a1) * math.sin(a2) * math.cos(b1) * math.sin(b2)  
	t3 = math.sin(a1) * math.sin(b1)  
	tt = math.acos(t1 + t2 + t3)  
	dis =  6366000 * tt 
	return dis
def sendweixin(msg):
	#msg = '%s car is comming' % data[0]
        weixin.login('linuxu2015@gmail.com','Xlb890213')
        weixin.singlesend('oZE9Gv2DJURwE6WY8HZ0bENqhVW4',msg)
def post(data):
	url = 'http://ytbus.jiaodong.cn:4990/BusPosition.asmx/GetBusLineStatus'
	res = session.post(url,data[2])
	position = res.text.split('>')[2].split('<')[0]
   	jsondata = json.loads(position)
        for i in range(len(jsondata)):
	#	print jsondata[i]
		x = float(jsondata[i]['GPSX'])
		y = float(jsondata[i]['GPSY'])
		pai = jsondata[i].values()[3]
		station = jsondata[i].values()[2]
		ID = jsondata[i].values()[4]
		a,b = getbaiduxyz(x,y)
		line = data[0]
#		print pai,a,b,ID,station,line
		paiu = pai.encode('utf-8')
		IDu = ID.encode('utf-8')
		stationu = station.encode('utf-8')
#		print type(paiu),type(stationu),type(IDu)
		t = time.strftime(ISOTIMEFORMAT,time.localtime(time.time()))
		insert(pai,a,b,ID,station,line,t)
		dis = circle(a,b)
		if dis < 2000  and b > 37.466839 and a > 121.444287:
			msg = '%s %s路 距离上车点 %f 米 可以上车' % (pai,data[0],dis)
#			sendweixin(msg)		
			#if data[1] == 0:
		#	print '%s %s路 距离上车点 %f 米 可以上车' % (pai,data[0],dis)
		#	data[1] = 1
		#else:
	#		print '%s %s路 距离上车点%f 米' % (pai,data[0],dis)
data = [86,0,'stationID=3327&lineID=50&lineStatus=2&userRole=1',[]]
data19 = [19,0,'stationID=49&lineID=57&lineStatus=2&userRole=1',[]]
n = 0
while True:
#	print '###################################'
	post(data)
	post(data19)
	time.sleep(10)
 #       n = n + 1
  #      if n > 2:
#		data[1] = 0
#		data19[1] = 0
#		n = 0
