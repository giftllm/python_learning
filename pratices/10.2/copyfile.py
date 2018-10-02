import sys
if len(sys.argv) < 3:
    print("Wrong paramter")
    print("./copyfile.py file1 file2")
    sys.exit()
f1 = open(sys.argv[1])
s = f1.read()
f1.close()
f2 = open(sys.argvp[2], 'w')
f2.write(s)
f2.close()

print("First value", sys.argv[0])
print("all value")
for i in enumerate(sys.argv):
    print(i, x)

