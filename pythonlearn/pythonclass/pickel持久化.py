#coding:utf-8
import pickle as p
shoplistfile = 'shoplist.data'
shoplist = ['1','2','3']
f = file(shoplistfile,'w')
p.dump(shoplist,f)
f.close()
del shoplist
f = file(shoplistfile)
storedlist = p.load(f)
print storedlist