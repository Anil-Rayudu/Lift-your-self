def longstr(x):
    a=x.split(" ")
    res=""
    for i in a:
        if len(i)>len(res):
            res=i
    return res
print (longstr(input()))