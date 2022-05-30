test_list=[4,6,4,3,3,4,3,4,3,8]
uniqu=list(set(test_list))
res=[]
for i in uniqu:
    if test_list.count(i)>3:
        res.append(i) 
print (res)