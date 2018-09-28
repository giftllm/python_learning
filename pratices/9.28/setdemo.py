s = set([1,2,3])    #要创建一个set，需要提供一个list作为输入集合
print(s)
s.add(4)
print(s)

s.remove(4)
print(s)
#set可以看成数学意义上的无序和无重复元素的集合
s1 = set([1,2,3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
