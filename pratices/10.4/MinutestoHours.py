#请在 /home/shiyanlou/Code写出一个 MinutesToHours.py 脚本文件，实现一个函数 Hours()，将用户输入的 分钟数
# 转化为 小时数和分钟数，并要求小时数尽量大。将结果以 XX H, XX M 的形式打印出来。(注意打印格式中的空格)
'''import math
import sys
def Hours(minutes):
    hours = 0
    minutes = minutes
    hours = int(minutes / 60)
    minutes = int(minutes % 60)
    print("{:d} H, {:d},M",format(hours, minutes))
hours = 0
minutes = 0


inValue = int(sys.argv[1])

try:
    if inValue.isdigit():
        minutes = int(sys.argv[1])
        if minuntes < 0:
            raise ValueError("Input nmber can't be negative")
        else:
            Hours(minutes)

    elif '-' == inValue[0] and inValue.lstrip('-').isdigit:
        raise ValueError("Input number can't be negative")
r
except ValueError:
    print("ValueError: Input number can't be negative")
'''
'''
try:
    m = int(sys.argv[1])
    if m < 0:
        raise ValueError("A ValueError happend")
    else:
        Hours(minutes)
except ValueError:
    print("ValueError! ")
'''

import sys
minutes = int(sys.argv[1])


if len(sys.argv) < 2:
    print("please input numbers:")
def Hours():
    global minutes
    if minutes < 0:
        raise  ValueError
try:
    Hours()
except ValueError:
    print("ValueError: input number can't be negative")
else:
    H = minutes / 60
    M = minutes % 60
    print("{} H, {} M".format(H,M))