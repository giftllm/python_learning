#计算数列 1/x+1/(x+1)+1/(x+2)+ ... +1/n，我们设 x = 1，n = 10
sum = 0
for i in range(1,11):
    sum += 1.0 / i
    print("{:2d} {:3.3f}".format(i, sum))

#一元二次方程的在写
import math
a = int(input('Enter value a'))
b = int(input('Enter value b'))
c = int(input('Enter value c'))
d = b * b - 4 * a * c
if d < 0:
    print('wujie')
else:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    if root1 == root2:
        print("root1 = root2 = ", root1)
    else:
        print("root1 = ", root1)
        print('root2 = ', root2)
