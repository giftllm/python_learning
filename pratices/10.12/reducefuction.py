# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 对一个序列做求和：
from functools import reduce #从functools库中引用 reduce函数
def add(x, y):#定义一个add（x, y）函数
    return x + y #返回值x + y
print(reduce(add, [1,3,5,7]))   #reduce(function, sequence[, initial]) -> value reduce（）函数两个参数，第一个add函数，第二个参数是一个序列

#把序列[1, 3, 5, 7, 9]变换成整数13579

def fn(x, y): #定义函数fn（）
    return x*10 + y #返回值为x*10+y，按照resuce（）函数的用法，reduce（fn，[1,3,5,7,9]),= f(f(f(1,3),5),7),f（1,3）=13，
    # f（13,5）=135，f（135,7）= 1357.。。。
print(reduce(fn, [1,3,5,7,9]))



