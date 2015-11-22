#coding:utf-8
class Person:
    def __init__(self,name):
        self.name = name
    def sayHi(self):
        print('Hello,how are you?,my name is %s' % self.name)

p = Person('Swaroop')
print(p)
p.sayHi()