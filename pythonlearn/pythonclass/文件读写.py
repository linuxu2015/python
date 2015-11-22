#coding:utf-8
string = '''ahhaha
hahha
hhahha
jjaakkaka'''
f = file('file','w')
f.write(string)
f.close()
f = file('file')
while True:
    line  = f.readline()
    if len(line) == 0:
        break
    else:
        print line,
f.close()