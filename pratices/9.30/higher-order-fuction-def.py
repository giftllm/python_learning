'''
高阶函数（Higher-order function）或仿函数（functor）是内部至少含有一个以上步骤的函数：

使用一个或多个函数作为参数
返回另一个函数作为输出
Python 里的任何函数都可以作为高阶函数。
'''
def high(func, value):
    return func(value)
list = high(dir, int)
print(list[-3:])
