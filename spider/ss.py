#!/usr/bin/env python
#coding:utf-8
from  pyquery  import PyQuery as pq
import weixin
import requests
url = 'http://www.ishadowsocks.com'
key = '.col-lg-4.text-center'
r = requests.get(url)
p = pq(r.text).find(key)
n = 0
msg = ''
for i in p:
    if n <3:
        q = pq(i).text()
        s = q.split(':')
        #print  'proxy = ss://%s:%s@%s:%s' %(s[4].split(' ')[0],s[3].split(' ')[0],s[1].split(' ')[0],s[2].split(' ')[0])
	if  s[3].split(' ')[0]:
        	msg = msg + 'proxy = ss://%s:%s@%s:%s\n' %(s[4].split(' ')[0],s[3].split(' ')[0],s[1].split(' ')[0],s[2].split(' ')[0])
	print s[3].split(' ')[0]
    n = n + 1
f = open('/root/.meow/rc','w')
f.writelines('msg')
f.close()
print msg
#weixin.login('linuxu2015@gmail.com','Xlb890213') 
#weixin.singlesend('oZE9Gv2DJURwE6WY8HZ0bENqhVW4',msg)
