'''
:map 是一个在 Python 里非常有用的高阶函数。它接受一个函数和一个序列（迭代器）作为输入，
然后对序列（迭代器）的每一个值应用这个函数，返回一个序列（迭代器），其包含应用函数后的结果。
'''
lst = [1, 2, 3, 4, 5]
def square(num):
    print("返回所给数的平方")   #循环几次
    return num * num
print(list(map(square, lst)))
