'''
def mult(a, b):
    zip_b = zip(*b)
    #return [[sum(ele_a * ele_b for ele_a , ele_b in zip(row_a, col_b)) for col_b in zip_b] for row_a in a]
    x = [[1,2,3],[4,5,6],[7,8,9,][9,10,11,12]]
    y = [1,2],[1,2]
    print(mutl(x, y))
'''
'''
import numpy as np  
mx = np.matrix(x)
my = np.matrix(y)
print(mx*my)
'''