# -*- coding=utf-8 -*-
#函数的参数
#位置参数
#定义x平方的函数
def power(x):   #定义一个函数用def，power是函数名，x是函数变量，冒号一定不能少，不然编译出错
    return x * x    #函数的返回值用return语句返回

print(power(5)) #输出结果，其中power（5）是直接引用之前定义的power函数，用print（）来打印

#如果是x的n次方，怎么定义函数
def power_n(x, n): #定义一个power_n的函数,且函数中有两个变量，x和n
    s = 1   #先定义一个变量s，s 的值为初始赋值为1
    while n > 0:    #使用while 语句，给定条件n必须大于0才能执行
        n = n - 1   #每循环一次，n的值减1，直到n的值变为0，循环中断
        s = s * x   #s的值初始为1，把x的值赋值给s，下一次再循环就是x的平方，
    return s    #while语句执行完，返回s的值
print(power_n(5, 3))
# print(power_n(5)) 这行代码的运行结果是：TypeError: power_n() missing 1 required positional argument: 'n'
#power_n(x, n) 里面有两个值，引用power_n()函数就必须赋予两个值

#默认参数
#上面一个程序，如果定义power_n时，先定义n = 2，则n为默认参数
def power_m(x, n = 2):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s
print(power_m(5))
print(power_m(5,2)) #使用默认参数，两种输出结果是一样的
print(power_m(5, 3))    #对于n大于2的情况，必须输入n的值，不能省略
#默认参数可以简化函数的调用
'''设置默认参数时，有几点要注意：
一是必选参数在前，默认参数在后，否则Python的解释器会报错
二是如何设置默认参数。
当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数
'''
#ex:一年级小学生注册的函数，需要传入name和gender两个参数
def enroll(name, gender):   #定义enroll函数
    print('name:', name)     #美化输出格式
    print('gender:', gender)    #
print(enroll('Sa', 'F'))    #打印学生名字和性别

#如果要继续传入年龄和城市信息怎么办？
def enroll_more(name, gender, age = 6, city = 'Beijing'):   #设置年龄的默认值为6岁，城市默认为北京
    print('name:', name)
    print('gender:', gender)
    print('Age:', age)
    print('City', city)

print(enroll_more('xiaoming', 'F'))     #因为设置了默认参数，age和city取值默认参数
print(enroll_more('xiaohong','M','7', 'Shanghai'))      #函数enroll_more里面传入age和city的值

#默认参数有个最大的坑
#ex:

def add_end(L = []):    #定义函数add_end，参数L = []
    L.append('END')     #L.append()，向list里面添加对象
    return L
print(add_end([1,2,3]))
print(add_end())
print(add_end())    #默认参数是L = []即[]，后面执行两次add_end()，结果不一样
    #[]是一个变量，每次调用add_end()函数，如果改变了L的内容，则下次调用时，默认参数的值就改变
#  默认参数必须指向不变对象！
# 可变参数
#给定一组数字a，b，c……，请计算a2 +b2+ c2 + ……。
def calc(numbers):  #定义calc函数，里面变量为numbers
    sum = 0     #定义一个变量sum 初始赋值0
    for n in numbers:   #使用for循环，变量n使用变量numbers里面的所有值循环一遍for循环里面的代码
        sum = sum + n * n       #没经过一次循环，sum的值变为sum+n*n
    return sum          #返回sum的值

print(calc([1,2,3]))
print(calc((1,2,3)))        #调用calc函数时，需要先把calc组装成list或者tuple形式，否则编译出错


#把函数的参数改为可变参数：
def calc_1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc_1(1,2,3))        #相比之前的函数calc，calc_1使用print减少了一个双括号，使用更简单
print(calc_1())             #可以传入任意一个参数，包括0个参数

nums = [1,2,3]
print(calc_1(*nums))      #Python允许在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去

#关键字参数：关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
#ex：
def person(name, age, **kw):        #定义person函数，注意加冒号！**kw是关键字参数
    print('name:', name, 'age:', age, 'other:', kw)   #打印名字，年龄，和其他信息

print(person('Michel', 30))     #可以直接引用函数person！之前一直都以为只有print才能输出结果
print(person('Bob', 35, city = 'Beijing'))
person('LL', 31)

extra = {'city': 'Beijing', 'Job':"Engineer"}
person('Jack', 24, **extra)     #**extra表示吧extra这个字典里面的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个字典，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

#命名关键字参数：对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查

def person_key(name, age, **kwargs):        #注意加冒号！
    if city in kwargs:      #if判断语句，如果kwargs字典里面有city这个value，则执行下面的语句
        pass
    if job in kwargs:       #同上
        pass
    print('name', name, 'age', age, 'other', kwargs)

person('Jaca', 24, city = 'Beijing', addr = 'chaoyang', zipcode = '100010') #调用者仍可以传入不受限制的关键字参数

#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数

def person_name(name, age, *, city, job):
    print(name, age, city, job)

person_name("java", 24, city = 'Beijing', job = 'Engineer')      #命名关键字参数必须传入参数名
#person('java', 24, 'Beijing') 如果这样写，运行结果：TypeError: person() takes 2 positional arguments but 3 were given
#由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person_name()函数仅接受2个位置参数

#参数组合：可以用位置参数、默认参数、可变参数、关键字参数和命名关键字参数，5种参数组合使用

def f1(a, b, c = 0, *args, **kwargs):   #函数f1种有位置参数a b，默认参数c，可变参数args，关键字参数kwargs
    print('a = ', a, 'b = ', b, 'c = ', c, 'args = ', args, 'kwargs = ', kwargs)

def f2(a, b, c = 0, *, d, **kwargs):    #函数f2种有位置参数，默认参数，命名关键字参数，关键字参数
    print('a = ', a, 'b = ', b, 'c = ', c, 'd = ', d, 'kwargs = ', kwargs)

f1(1,2)     #输出结果:a =  1 b =  2 c =  0 args =  () kwargs =  {}，a,b,作为位置参数，1和2的值赋给a和b
f1(1,2, c = 3)      #输出结果：a =  1 b =  2 c =  0 args =  () kwargs =  {}， c作为默认参数，3的值赋给c
f1(1,2,3,'a','b')       #输出结果：a =  1 b =  2 c =  3 args =  ('a', 'b') kwargs =  {}，'a'和'b'作为可变参数，赋给args
f1(1, 2, 3, 'a', 'b', x=99) #输出结果：a =  1 b =  2 c =  3 args =  ('a', 'b') kwargs =  {'x': 99}，kwargs作为关键字参数，x = 99赋给kwargs
f2(1, 2, d=99, ext=None)    #输出结果：a =  1 b =  2 c =  0 d =  99 kwargs =  {'ext': None}，c作为默认参数，值为0， d作为命名关键字参数，
# d=99全部赋给d，所以输出结果为d = 99，kwargs作为命名关键字参数里面的关键字参数，输出结果是字典形式

args = (1, 2, 3, 4)
kwargs = {'d': 99, 'x': '#'}
f1(*args, **kwargs) #输出结果：a =  1 b =  2 c =  3 args =  (4,) kwargs =  {'d': 99, 'x': '#'} #可变参数args，先把1,2,3赋值给a,b,c,最后args的值是4，
# 并且以tuple形式输出，关键字参数kwargs输出结果不变

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw) #输出结果：a =  1 b =  2 c =  3 d =  88 kwargs =  {'x': '#'} 可变参数args，先把1,2,3赋值给a b c
# ,按照序列，命名关键字参数d = 88，关键字参数kwargs 的输出结果则为{'x'：'#'}













