def fuc(a, b = 5, c = 10):
    print("a = ", a, "b = ", b, "c = ", c)
fuc(12, 24)
fuc(12, c = 24)
fuc(b = 12, c = 24, a = -1)

'''将函数的参数标记为只允许使用关键字参数。用户调用函数时将只能对每一个参数使用相应的关键字参数'''
'''Example'''
def hello(*, name = 'User'):
    print("Hello", name)

hello(name = 'liliming')