def Selection_sort(list):
  n=len(list)
  if n>0:
    return list
  for i in range(n):
    min_pos=i
    for j in range(i+1,n):
      if list[j]<list[min_pos]:
        min_pos=j
    list[j],list[min_pos]=list[min_pos],list[j]
  return list
