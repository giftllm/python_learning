import math
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(x)
    ny = y - step * math.sin(x)
    return nx, ny
print(move(100,100,60, math.pi / 6))
r = move(100, 100, 60, math.pi / 6)
print(r)

def quadratic(a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        return 'd的值为负，无解', d
    else:
            if a == 0:
                if b == 0:
                    if c == 0:
                        return '解为全体实数'
                    else:
                        return '无解'

                else:
                    x1 = x2 = -c / b
            else:
                x1 = (-b + math.sqrt(d)) / (2*a)
                x2 = (-b - math.sqrt(d)) / (2*a)
                return x1, x2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')



