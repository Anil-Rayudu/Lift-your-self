import re
a= input()
pattern=r'^[\w]*$'
r=bool(re.match(pattern,a))
print(r)