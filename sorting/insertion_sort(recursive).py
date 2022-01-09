def insert(list,value):
  n=len(list)
  if  n==0:
    return value
  if v==list[-1]:
    return list+[v]
  else:
    return insert(list[:-1],v),list[-1:])
 def issort(list):
    n=len(list)
    if n<1:
      return list
    l=insert(issort(list[:-1],list[-1:]
    return l
