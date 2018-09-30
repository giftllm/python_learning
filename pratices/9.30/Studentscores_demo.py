# 判断学生成绩是否达标的程序
n = int(input("Enter the number of student:"))
data = {}
subjects = ('physici', 'math', 'history')
for i in range(0 , n):
    name = input("Enter the student {}:".format(i + 1))
    mark = []
    for x in subjects:
        mark.append(int(input("Enter marks of {}:".format(x))))
    data[name] = mark
for x, y in data.items():
    total = sum(y)
    print("{}'s total marks {}".format(x, total))
    if total < 180:
        print(x, "Failed")
    else:
        print(x, 'Passed')



