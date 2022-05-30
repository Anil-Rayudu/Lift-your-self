import numpy as np
def mat(x):
    a=np.ones((x,x),dtype=int)
    a[:,:]=5
    a[1:-1,1:-1]=2
    return a
print(mat(int(input()))) 