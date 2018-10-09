'''
class MyClass(object):
    i = 12345
    def f(self):
        return "hello world"
x = MyClass()


class Complexe:
    def __int__(self, rearpart, imagpart):
        self.r = rearpart
        self.i = imagpart
x = Complexe(1,1)
s

class nameoftheclass(parent_class):
    statement1
    statement3
    statement3

'''

class Person(object):
    def __init__(self, name):
        self.name = name

    def get_detials(self):
        return self.name

class Student(Person):
    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        return "{} student {} is in {} yaer,".format(self.name, self.branch, self.year)

class Tearch(Person):
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_detials(self):
        return "{} tesrchs {}".format(self.name, ',' .join(self.papers))


person1 = Person('Sachin')
student1 = Student('Kusha', 'CSE', 2006)
tearch1 = Tearch('Para', ['C', 'C++'])

print(person1.get_detials())
print(student1.get_details())
print(tearch1.get_detials())

'''
这个例子表达了父类和子类的关系，子类可以继承父类的方法，并且在子类中可以重写父类的方法，当调用子类参数时
使用的是各自子类的类方法。
'''







