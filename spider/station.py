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
start_station = ''
arrive_station = ''
date = ''
#url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=%s&from_station=%s&to_station=%s' %(date,start_station,arrive_station)
url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8902'
session = requests.Session()
#session.proxies = {'http': 'ss://aes-256-cfb:13814681@us1.iss.tf:443',
#                   'https': 'ss://aes-256-cfb:13814681@us1.iss.tf:443'}
session.header = {
		'Accept':'text/css,*/*;q=0.1',
		'Accept-Encoding':'gzip, deflate, sdch',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'Cache-Control':'max-age=0',
		'Connection':'keep-alive',
		'Cookie':'__NRF=DF03E9118750FD5BA40AD0A1F5CB99EE; JSESSIONID=0A02F009989FD8BCD926B0C77AD3318629B8A23297; BIGipServerotn=166724106.38945.0000; _jc_save_fromStation=%u70DF%u53F0%2CYAK; _jc_save_toStation=%u6D4E%u5357%2CJNK; _jc_save_fromDate=2016-02-01; _jc_save_wfdc_flag=dc',
		'Host':'kyfw.12306.cn',
		'If-Modified-Since':'Tue, 15 Dec 2015 22:40:49 GMT',
		'Referer':'https://kyfw.12306.cn/otn/lcxxcx/init',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'
                    }
r = session.get(url)
data = r.text
print data
datastr = str(data)
print datastr.split('|')
#print jsondata['data']['datas'][0]['start_station_name']
