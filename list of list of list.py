lst=[]
for i in range(2):
    lst.append([])
    for j in range(2):
        lst[i].append([])
        for k in range(3):
            lst[i][j].append(k+1.0)
print (lst)
