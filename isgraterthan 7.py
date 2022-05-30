def isgrthan_7(x):
    res=list(filter(lambda a:a>7,x))
    return res
print(isgrthan_7(list(map(int,input("enter the space seperated numbers : ").split()))))