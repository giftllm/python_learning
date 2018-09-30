for i , j in enumerate(['a', 'b', 'c']):
    print(i, j)
a = ['aaa', 'bbb']
b = ['ccc', 'ddd']
for x, y in zip(a, b):
    print("{} user {}".format(x, y))

'''
许多时候我们需要往字典中的元素添加数据，我们首先要判断这个元素是否存在，不存在则创建一个默认值。
如果在循环里执行这个操作，每次迭代都需要判断一次，降低程序性能。
我们可以使用 dict.setdefault(key, default) 更有效率的完成这个事情
'''
date = {'color':[]}
date.setdefault('names',[]).append('Ruby')
print(date)
date.setdefault('names', []).append('Python')
print(date)
date.setdefault('names', []).append('C')
print(date)

#
