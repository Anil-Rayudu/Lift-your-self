def add_it_up(x):
    lst=[]
    for i in range(int(x+1)):
        lst.append(i)
    return sum(lst)
print(add_it_up(int(input("Input the number upto which we need to add up : "))))