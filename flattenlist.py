from functools import reduce
a=[[1],[2,3],[4,5,6]]
#print(reduce(lambda x,y:x+y,a))
lst=[x for i in a for x in i]
print (lst)
#print(sum(a,[]))