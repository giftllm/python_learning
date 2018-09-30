def change():   #定义change（）函数
    #a = 90
    global a
    a = 90
    print(a)
a = 9
print("Before the fuction call ", a)
print("Inside change fuction ", end = '')
change()
print("After the fuction call", a)
'''全局变量和局部变量的区别'''
'''有默认值的参数后面不能再有普通参数，f（a, b = 90, c）这样的定义是错误的；默认值只被赋予一次，默认值是任何可变对象时会有所不同。'''
'''Example'''
def f(a, data = []):
    data.append(a)
    return data
print(f(1))
print(f(2))
print(f(3))

def g(b, data = None):
    if data == None:
        data = []
    data.append(b)
    return data
print(g(1))
print(g(2))
print(g(3))
