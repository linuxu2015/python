#!/usr/bin/env python
#coding:utf-8
from flask import Flask,jsonify,render_template,request
app =  Flask(__name__)
@app.route('/',methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        n = [request.form.get(x,0,type=float) for x in {'n1','n2','n3'}]
        return jsonify(max=max(n),min=min(n))
    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0')
