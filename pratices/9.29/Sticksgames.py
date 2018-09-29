#  有 21 根棍子，首先用户选 1 到 4 根棍子，然后电脑选 1到 4 根棍子。谁选到最后一根棍子谁就输。你知道哪种情况用户会赢吗？
# 特别说明：用户和电脑一次选的棍子总数只能是5

sticks = 21
print("there are 21 sticks , you can take 1-4 number of sticks at one time")
print("whoever will take the last stick will lose")
while True:
    print("Sticks left: ", sticks)
    sticks_taken =  int(input("Take sticke(1-4):"))
    if sticks == 1:
        print("you took the last stick, you loose")
        break
    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Wrong choice")
        continue
    print("computer took:", (5-sticks_taken), "\n")
    sticks -= 5
#  stick_taken x y m n  i j 常用的一些变量
