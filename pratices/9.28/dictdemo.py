d = {'Micheel':95, 'Bob':75, "Tracy":85}
print(d['Micheel'])
# 字典用大括号。。。
d['Bob'] = 88
print(d['Bob'])
#如果key不存在，dict就会报错
#print(d['Jcak'])
d.get('Tracy')
print(d.get('Tracy'))
print(d.get('Tracy', 0))
print(d.get('Jack',0)) #dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print(d.pop('Bob'))