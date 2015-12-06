#!/usr/bin/env python
#coding:utf-8
import re
import os
import time
import urllib
import urllib2
import requests
from bs4 import BeautifulSoup
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
import MySQLdb as mysql
db = mysql.connect(user='root',passwd='112613',db='python',host='127.0.0.1',use_unicode=True,charset='utf8')
db.autocommit(True)
cur = db.cursor()
start_station = 'YAK'
arrive_station = 'JNK'
date = '2016-02-01'
url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=%s&from_station=%s&to_station=%s' %(date,start_station,arrive_station)
session = requests.Session()
session.header = {
		'Accept':'text/css,*/*;q=0.1',
		'Accept-Encoding':'gzip, deflate, sdch',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'Cache-Control':'max-age=0',
		'Connection':'keep-alive',
#   		'Cookie':'__NRF=DF03E9118750FD5BA40AD0A1F5CB99EE; JSESSIONID=0A02F009989FD8BCD926B0C77AD3318629B8A23297; BIGipServerotn=166724106.38945.0000; _jc_save_fromStation=%u70DF%u53F0%2CYAK; _jc_save_toStation=%u6D4E%u5357%2CJNK; _jc_save_fromDate=2016-02-01; _jc_save_wfdc_flag=dc',
                'Cookie':'JSESSIONID=0A02F00760C02CD20F5EDC1357C3E9AE446A7AFB60; __NRF=65C1BB0C7B217320825E6500EC86091E; BIGipServerotn=133169674.24610.0000; _jc_save_fromStation=%u70DF%u53F0%2CYAK; _jc_save_toStation=%u6D4E%u5357%2CJNK; _jc_save_fromDate=2016-01-30; _jc_save_wfdc_flag=dc',
		'Host':'kyfw.12306.cn',
		'If-Modified-Since':'Tue, 15 Dec 2015 22:40:49 GMT',
		'Referer':'https://kyfw.12306.cn/otn/lcxxcx/init',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'
                    }
r = session.get(url)
#print r.text
jsondata = json.loads(r.text)
#print jsondata['data']['datas'][0]['start_station_name']
def listtrain():
	for i in range(0,len(jsondata['data']['datas'])):
		realdata = jsondata['data']['datas'][i]
		station_train_code = realdata['station_train_code']
		start_station_name = realdata['start_station_name']
		end_station_name = realdata['end_station_name']
		from_station_name = realdata['from_station_name']
		to_station_name = realdata['to_station_name']
		start_time = realdata['start_time']
		arrive_time = realdata['arrive_time']
		train_class_name = realdata['train_class_name']
		lishi = realdata['lishi']
		zy = realdata['zy_num']
		ze = realdata['ze_num']
		yz = realdata['rz_num']
		yw = realdata['yw_num']
		wz = realdata['wz_num']
		s =  '车次：%s 始发站:%s 终点站:%s 上车站:%s 下车站:%s 开车时间:%s 到达时间:%s 车辆类型:%s 历时:%s 一等座:%s 二等座:%s 硬座:%s 硬卧:%s 无座:%s' %(station_train_code,start_station_name,end_station_name,from_station_name,to_station_name,start_time,arrive_time,train_class_name,lishi,zy,ze,yz,yw,wz)
                #return s
                sql = "insert into train (station_train_code,start_station_name,end_station_name,from_station_name,to_station_name,start_time,arrive_time,train_class_name,lishi,zy,ze,yz,yw,wz) value ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(station_train_code,start_station_name,end_station_name,from_station_name,to_station_name,start_time,arrive_time,train_class_name,lishi,zy,ze,yz,yw,wz)
#                sql = "insert into train (station_train_code,start_station_name,end_station_name,from_station_name,to_station_name,start_time,arrive_time,train_class_name,lishi,zy,ze,yz,yw,wz) value ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(1,1,1,1,1,1,1,1,1,1,1,1,1,1)
                cur.execute(sql)
while True:
        listtrain()
	time.sleep(5)
