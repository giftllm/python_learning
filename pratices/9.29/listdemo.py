'''squar = []
for x in range(10):
    squar.append(x ** 2)
print(squar)
'''
'''
squar = list(map(lambda x : x ** 2, range(10)))
print(squar)
map map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，
得到一个新的 list 并返回。

lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。
lambda所表示的匿名函数的内容应该是很简单的，如果复杂的话，干脆就重新定义一个函数了，使用lambda就有点过于执拗了。
lambda就是用来定义一个匿名函数的，如果还要给他绑定一个名字的话，就会显得有点画蛇添足，通常是直接使用lambda函数。如下所示：
add = lambda x, y : x+y
add(1,2)  # 结果为3
1.Python提供了很多函数式编程的特性，如：map、reduce、filter、sorted等这些函数都支持函数作为参数，
lambda函数就可以应用在函数式编程中
2.应用在闭包中
'''
'''squar = [x ** 2 for x in range(10)]
print(squar)
'''
'''
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)
'''
combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combs)

# 二次函数 y = x*x + 1  x = [1, 2, 3]

a = [1, 2, 3]
for x in a:
    x = x ** 2 + 1
    l = []
    l.append(x)
    lst = []
    lst.extend(l)
    print(lst   )

    #print(x.append(x), end =' ')
    #下面程序输出结果是列表形式，这个程序输出结果是数值类型。哪里不对呢，我想把这个程序的输出结果也以类表形式输出，怎么办？

#z = [x + 1 for x in [x ** 2 for x in [1, 2, 3]]]
#print(z)