def insertion_sort(list):
  n=len(list)
  if n<1:
    return list
  for i in range(n):
    j=i
    while j>0 and list[j]<list{j-1]:
         list[j],list[j-1]=list[j-1],list[j]
         j=j-1
  return list
