import re
lst=["Apple","Bannana","Gauva","Orange","Mango"]
res=[]
pattern=r'^[AEIOUaeiou].*$'
for i in lst:
    if re.match(pattern,i):
       res.append(i)
print(res) 