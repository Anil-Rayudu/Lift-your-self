import numpy as np
def mult_5(x):
    a=np.arange(5,5*x+1,5)
    return a
print(mult_5(int(input("Input the number of multiples 0f 5 are requires : "))))