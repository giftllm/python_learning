#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
from functools import reduce #reduce引用
def prod(x,y):  #定义prod（）函数
    return x*y #返回值x*y
L = reduce(prod,[1,2,3])    #reduce(prod,[1,2,3])等价于 prod（prod（1,2），3）
print(L)
print(reduce(prod,[1,2,3]))

