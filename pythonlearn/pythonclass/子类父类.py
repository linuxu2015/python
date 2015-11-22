# coding:utf-8
class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        print 'Name:%s Age:%s' % (self.name, self.age),


class Teacher(SchoolMember):
    def __init__(self, name, age, money):
        ##集成父类的name和age属性
        SchoolMember.__init__(self, name, age)
        self.money = money

    def tell(self):
        SchoolMember.tell(self)
        print 'money:%s' % self.money


class Student(SchoolMember):
    def __init__(self, name, age, score):
        SchoolMember.__init__(self, name, age)
        self.score = score

    def tell(self):
        SchoolMember.tell(self)
        print 'score:%s' % self.score


t1 = Teacher('TOM', '34', '4000')
s1 = Student('JIM', '20', '90')
# t1.tell()
member = [t1, s1]
for i in member:
    i.tell()
