#!/usr/bin/env python
#coding:utf-8
import re
import os
import time
import urllib
import urllib2
import requests
from bs4 import BeautifulSoup
def saveImage(imgurl,imgName = 'default.jpg'):
    response = requests.get(imgurl,stream=True,proxies = proxies,verify = False)
    image = response.content
    #DstDir = "F:\\image\\"
    DstDir = "/root/img/"
    print "save"
    with open(DstDir+imgName ,"wb") as jpg:
        jpg.write(image)     
        return
    jpg.close
#url = 'http://t66y.com/htm_data/2/1601/1819426.html'
url = 'http://t66y.com/htm_data/2/1601/1819717.html'
#url = 'http://www.baidu.com'
session = requests.Session()
#session.proxies = {'http': 'ss://aes-256-cfb:13814681@us1.iss.tf:443',
#                   'https': 'ss://aes-256-cfb:13814681@us1.iss.tf:443'}
proxies = { 'http': 'http://192.168.70.215:8787',
            'https': 'https://192.168.70.215:8787' }
session.header = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Cache-Control':'max-age=0',
            'Cookie':'__cfduid=df3c922ba6a3f5693716c2b43ab6e80dc1452256579;227c9_lastfid=0;227c9_lastvisit=0%091452256777%09%2Fread.php%3Ftid%3D1791021;CNZZDATA950900=cnzz_eid%3D931396561-1452252229-http%253A%252F%252Ft66y.com%252F%26ntime%3D1454066847',
            'Host':'t66y.com',
            'If-Modified-Since':'Fri, 29 Jan 2016 11:47:27 GMT',
            'If-None-Match':'W/"2829168-1406c-52a77996cb5af"',
            'Proxy-Connection':'keep-alive',
            'Referer':'http://t66y.com/thread0806.php?fid=2',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
                    }
r = session.get(url,proxies = proxies,verify = False)
#print r.text
#r = urllib2.urlopen(url).read()
#print r
filelist = []
soup = BeautifulSoup(r.text)
for photo in soup.find_all('img'):
    filelist.append(photo.get('src'))
#print filelist
for i in range(len(filelist)):
    imgurl = filelist[i]
    imgname = imgurl.split('/')[-1]
    #print imgname
    #print imgurl
    saveImage(imgurl,imgname)
