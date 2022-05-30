from functools import reduce
def fact(x):
    res=reduce(lambda a,b:a*b , [a for a in range(1,x+1)] )
    return res
print (fact(int(input("Enter 4the number for which factorial need to be calculated :"))))