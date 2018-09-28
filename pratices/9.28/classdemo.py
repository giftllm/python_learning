#str是不变对象，而list是可变对象,字面意思理解
a = ['c', 'b', 'a']
a.sort()
print(a)


#str
a = 'abc'
b = a.replace('a', 'A')
print(a)
print(b)
