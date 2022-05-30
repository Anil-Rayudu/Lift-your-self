def swap(x):
    a,b=map(int,x.split())
    a=a+b
    b=a-b
    a=a-b
    return f"{a} {b}"
print( swap(input("Input two space seperated numbers to swap : ")))