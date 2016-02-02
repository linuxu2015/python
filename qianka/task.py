#!/usr/bin/env python
# coding:utf-8
import requests
import pickle
import json
import weixin
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
ISOTIMEFORMAT = '%Y-%m-%d %X'
session=requests.session() 
session.headers={
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate, sdch',
		'Accept-Language': 'zh-CN,zh;q=0.8',
		'Cache-Control': 'max-age=0',
		'Connection': 'keep-alive',
		'Cookie': 'PHPSESSID=c407ccf5ddae840c1800b280592db705c799ad8c; aliyungf_tc=AQAAANAvjgO1OgoAhjMFelKwzuToKarr; gaoshou_session=eyJpdiI6IkJhTWM4bHZyUEUyUGFSM1dMdHFEUmc9PSIsInZhbHVlIjoib3VkZ0VZWDBKXC9yUnNtd3ROU1ZKbnpwXC9mYU1keENjVlBOck1qdnVRcTFZQTVmKzlKNW1PMWU1dk9vcUs3U3NRNnhWZEsxcUxtTXZaVU1EVTZncld3Zz09IiwibWFjIjoiNjk2M2Y1NzViNWE3YjllY2U1N2Q4YmZlNzgzNGIzODFkY2RmMjY1ODNiNGI3ZDFkZGUwZjA2MDQ0MGRlYjU0YyJ9; qk:guid=c8aa3a50-bb82-11e5-8259-bb083e1d2775-20160115; qk_app_id=13; qk_ll=eyJpdiI6IjZldDdHMjJMTXZoR1FOZnhnTmY0UUE9PSIsInZhbHVlIjoiZlNFT09MXC9YM2Q3Rk83ZUQ0Z3dTaWc9PSIsIm1hYyI6ImZlNWM2NTkzZmEzMjE5ZDljMmJkODYwMTNiMTkyNzc4MGQwYzkwMzNhOTQyYzAzY2QwMzkzODViMzIwMGM0ZTgifQ%3D%3D; appid=13; hera=3927',
	#	'Cookie': 'aliyungf_tc=AQAAANOOzAP+tgQAhjMFeswIqj4Ds2tq; PHPSESSID=a4d2d3d273221ed652e2dec7e47ba2009aecc02d; gaoshou_session=eyJpdiI6ImRzWkF2bk9hN2M2SXpkdWk4ajNHcXc9PSIsInZhbHVlIjoiYlh6Q1ltdU1UY2pSRlFORFwvWGxkbm11XC9HeXNnRStGcTJydkQyOFwvbStPNys5RFk0M2JQemZYWXBaRk9EQkZSYkFVb0dHckNtcjRwNWJteXZKS2IrblE9PSIsIm1hYyI6IjcwYjM1YzQ1ODk3MGVjMjc4M2U1NjZlMGUzZTRmNjE3ODBmZWQ0M2JkYTUzYTA0YWMzMzEzM2Y5NjEzNTU2YzkifQ%3D%3D; qk:guid=8319af40-bf22-11e5-8584-a5f66212a099-20160120; qk_app_id=13',
	#	'Cookie':'qk:guid=8319af40-bf22-11e5-8584-a5f66212a099-20160120; qk_ll=eyJpdiI6IjRNcmYyQk9taWllMnU5K2d5SERWNmc9PSIsInZhbHVlIjoiYm1vTVV2VFdua0x6ZTNKUjFkS1o5Zz09IiwibWFjIjoiZTgwNzE5ZDQ0NzY4NjFmMzFmZDgyNzNlYmM4OTQzMzY0ZjJhMzJjNDlhYThiNWI1MGE1OTViZTE1MTQ5MTdmZSJ9; aliyungf_tc=AQAAAGyDwy8E7QkAhjMFeqpEfzkrc3Xj; gaoshou_session=eyJpdiI6InFrNjFaalRWQXVGNHNOYmVcL3p4K1NnPT0iLCJ2YWx1ZSI6IkRlSWM3cUZiQVA1VDQwcndpSCtnWTNaOFwvWlRxUVdGeDFiU3BzOXlyOUF5TDZoM2IrcnJObGozRlZxbE5jYjZUQnRSTERzd0ZqXC9HZFZFVmU1STVYeWc9PSIsIm1hYyI6IjQyN2E2NzRiY2M0YzhiZmFiMDk3ZWFhY2VhZDcyYTVkYjc3YTA0MWNiODJkZjY0NTkzMDEwMDIwYjg0NDhmNTgifQ%3D%3D; PHPSESSID=896bd914256cf3cb3d1aded3bd9cff1ac1c2bcee; qk_app_id=13; appid=13',
		#'Cookie': 'PHPSESSID=a4d2d3d273221ed652e2dec7e47ba2009aecc02d; qk:guid=8319af40-bf22-11e5-8584-a5f66212a099-20160120; qk_ll=eyJpdiI6Im9Wb2ZpZG91V2VYaUg1XC9FUDVJV0dnPT0iLCJ2YWx1ZSI6IktjKzFzajdqbjBnUmZ2QnRUZ3VWc1E9PSIsIm1hYyI6IjI4ZDRhNDlmMjNkYzA2OTVmZDAzNDM2ODhkYTBlOTg5NmI0NzgzN2FiZTVhNGQ2MDRmMWEzNzZjZGFkZmJiOTEifQ%3D%3D; aliyungf_tc=AQAAAL9gS2t6TgMAhjMFeqQVmS0JiFzE; gaoshou_session=eyJpdiI6IjlcLytFS0JUQlM5SnUzUU13N3dheTdnPT0iLCJ2YWx1ZSI6IkZvS3IyKzd6YVVXc3hDTFVLWWxhcVRrXC8rREpFVGczQ3A4azZHY3MrUU5cL2FmWHJRXC9rV0xhdW9vZjRoSnBxYU80d0hXa011VFlQZ2VcL01YT1JmVld6QT09IiwibWFjIjoiMTYwOGJjY2RhZjBhYjg0N2Q0ZDE1YzI1NjVlYjA1YTkzZTQwMGZmZGZmMTNiNTNhOTYxN2JlZTJlNTkzZjYxYyJ9; appid=8; qk_app_id=8',
###iphone 4s
	#	'Cookie': 'PHPSESSID=34ff56cdadd33985642ccd6dd55f479acf708d2c; aliyungf_tc=AQAAAFhJOjMU/wsA46DiemPIfEtwXWt8; gaoshou_session=eyJpdiI6IllvaVYwVVVnWUppTEhCQmhRNDU0emc9PSIsInZhbHVlIjoiMHVvWk55NXVPRSt0cXRxSlE4TGR1TEx3WndlRDBDWjRzVWdDUm13a1ViWWtNd1dRclRKZzRVeUlzclwvNlJQUkFqQzRwV1drUVM1NDJwS0htVGs3aldnPT0iLCJtYWMiOiI3ZTMxNGE3OWE1OTdlZTJjZDAwNGFiNjgyYWY4ZDk4YmNlZDk5NDViNDMzMTdlZDdkMjMyOWNhNmU5ZDM2YjZkIn0%3D; qk:guid=c8aa3a50-bb82-11e5-8259-bb083e1d2775-20160115; qk_app_id=13; qk_ll=eyJpdiI6Iit0NXAwckhcL1wvTlRadlVINXBCZkR5Zz09IiwidmFsdWUiOiJSeW5VdGFyTHB',
	#	'Cookie': 'qk:guid=44ed55f0-b603-11e5-ac8e-9b6d251328ab-20160108; PHPSESSID=1d96afb3970c49725f97281e876f95d43ab0ca7c; qk_app_id=13; qk_ll=eyJpdiI6IitXQXVwUERFUHRoVFN2cDRHYzhVcEE9PSIsInZhbHVlIjoiVGt2VzN4NWhnVlpXeVVaYkl1ejBBUT09IiwibWFjIjoiZTVhYzlkYjBkNWI5N2MyMDM2MWY1NTRjNjdkOWEzNDJlMmJjMWQzNDZjMDBhNDAwNDZhOWVlN2MyN2I0NjZhOCJ9; aliyungf_tc=AQAAANXZQ0gzCQIAACJRKj8vvWGUMb6J; gaoshou_session=eyJpdiI6InFFNmoyc3ROMmsyXC9sYXVVa0JPWU1BPT0iLCJ2YWx1ZSI6IlJqUzFpMXlGZGw0UzhCcGowTHpncjV0VVJoanBHSnNnWnIrNGFoaTV2bHRiYlwvRVlYR3poN25BbDNhUFJVWnJQcmtHRmJnbXkxeUdDUUc4QzEzdTZuQT09IiwibWFjIjoiYTcyYmRhNzk1YjdiNmZiODRmNjIwZTg0YmFkNTAwMzE1ODlkZWNkMTJkNmZkNGY0OTlhNDcyYmZlM2ZhMTgyZSJ9',
		'Host': 'm.qianka.com',
		'Referer': 'http://m.qianka.com/fe/dashboard/index.html?timestamp=1453208332253',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4'
		}
def qiang(data):
	url = 'http://m.qianka.com/api/h5/subtask/start_v2'
	res = session.post(url,data)
	res1 = session.post(url,data)
	#print json.loads(res.text)
        resdata = json.loads(res.text)
	res1data = json.loads(res1.text)
	msg = resdata['data']['msg'] + '####' + res1data['data']['msg']
	print msg
	#weixin.login('linuxu2015@gmail.com','Xlb890213')
	#weixin.singlesend('oZE9Gv2DJURwE6WY8HZ0bENqhVW4',msg)
def listtask():
	msg = '你抢到了一个任务'
	url='http://m.qianka.com/api/h5/subtask/fetch'
	res=session.get(url)
	#print res.text
        data = json.loads(res.text)
	for i in range(0,6):
		status = data['data'][i]['status']
	#	status = 2
		if status == 2:
			msg = msg + data['data'][i]['title']
			weixin.login('linuxu2015@gmail.com','Xlb890213')
			weixin.singlesend('oZE9Gv2DJURwE6WY8HZ0bENqhVW4',msg)
			print(msg)
			break
			#sys.exit()
	for j in range(0,3):
		task_title = data['data'][j]['title']
		task_id = data['data'][j]['id']
		task_qty = data['data'][j]['qty']
		print(task_title),
		print(task_id),
		print(task_qty)
	tid = data['data'][0]['id']
	taskid = str(tid)
        taskqty = data['data'][0]['qty']
	task = { 'task_id' : taskid }
	if taskqty > 0:
		qiang(task)
		print('#################################抢到了！！####################################')
	print(time.strftime(ISOTIMEFORMAT,time.localtime(time.time())))#while True:
#	if task == False:
listtask()
#		time.sleep(2)
#	else:
#		time.sleep(10)
	
