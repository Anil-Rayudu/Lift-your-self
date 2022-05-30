from functools import reduce
def sumofsquares(n):
    res=reduce(lambda x,y:x+y**2, range(1,n+1)) 
    return res
print(sumofsquares(int(input("Enter the number upto which sum of square of numbers is required : "))))