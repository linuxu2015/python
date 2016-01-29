#!/usr/bin/env python 
# coding:utf-8
import requests
import json
import weixin
import time
import sys
import re
import math
reload(sys)
sys.setdefaultencoding('utf-8')
ISOTIMEFORMAT = '%Y-%m-%d %X'
global x
global y
session=requests.session()
session.headers={
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding':'gzip, deflate, sdch',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'Cache-Control':'max-age=0',
		'Cookie':'BAIDUID=1274744F8D97ACCE310DB0CB6B406414:FG=1; BIDUPSID=1274744F8D97ACCE310DB0CB6B406414; PSTM=1453259157; BDUSS=2RvaExHbHhvWldVUDhTc2plZlR2NndvMVNhN3pGWXhkTWVkU2FBaDF4Sm9rTVpXQVFBQUFBJCQAAAAAAAAAAAEAAACfKVsHwOTM7LXEs-bX0wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGgDn1ZoA59WY; BDRCVFR[XGj0xmfqYMf]=mk3SLVN4HKm; H_PS_PSSID=1449_18879_17942_18964_18778_15504_12030_18981; MCITY=-%3A',
		'Host':'api.map.baidu.com',
		'Proxy-Connection':'keep-alive',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
                }
def getbaiduxyz(x,y):
	url = 'http://api.map.baidu.com/geoconv/v1/?coords=%s,%s&from=1&to=5&ak=BB8dfc15391c2ec2805b88c50dac7bcf' %(str(x),str(y))
#	print url
	res = session.get(url)
	#baidu = res.text
	jsondata  = json.loads(res.text) 
	a = jsondata['result'][0]['x']
	b = jsondata['result'][0]['y']
	url_p = 'http://api.map.baidu.com/trace/v2/track/addpoint'
	data = {'ak':'BB8dfc15391c2ec2805b88c50dac7bcf','service_id':'109556','entity_name':'86','latitude':b,'longitude':a,'coord_type':3,'loc_time':int(time.time())}
	#res1 = session.post(url_p,data)
	#j_d = json.loads(res1.text)
	return a,b

