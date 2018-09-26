#if 案例
#birth = input('birth:')
#birth = int(birth)
#if birth < 2000:
#	print('00前')
#else:
#	print('00后')


#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖

high = 1.75
weight = 80.5
BMI = weight/(high**2)
print("xiaoming's BMI is:", BMI)
if BMI >= 32:
	print("xiaoming's weight is server obesity")
elif BMI >=28:
	print("xiaoming's weight is obesity")
elif BMI >= 25:
	print("xiaoming's weight is fate")
elif BMI >= 18.5:
	print("xiaoming's weight is normal")
else:
	print("xiaoming's weight is too light")

print("xiaoming's BMI is: ", '%.2f'%BMI)

#BMI的数值怎么取小数点后两位,最后的取值方法：'%。2f'%BMI

