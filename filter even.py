def filter_eve(x):
    res=list(filter(lambda a:a%2==0, x))
    return res
print(filter_eve(list(map(int,input("enter the space sperated numbers of list to check even numbers : ").split()))))