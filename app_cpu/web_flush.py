#!/usr/bin/env python
from flask import Flask,render_template,request
import MySQLdb as mysql
con = mysql.connect(user='root',passwd='1qaz2wsx',db='python',host='192.168.70.193')
con.autocommit(True)
cur = con.cursor()
app = Flask(__name__)
import json
tmp_time = 0
@app.route('/')
def index():
    return render_template('test.html')
@app.route('/data')
def data():
    global tmp_time
    if tmp_time > 0:
        sql = 'select * from memory where time > %s' % (tmp_time/1000)
    else:
        sql = 'select * from memory'
    cur.execute(sql)
    arr = []
    for i in cur.fetchall():
        arr.append([i[1]*1000,i[0]])
    if len(arr)>0:
        tmp_time = arr[-1][0]
    return json.dumps(arr)
    #return arr
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)

