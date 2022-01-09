def binary_search(value,list):
  if list==[]:
    return False
  mid= len(list)//2
  if value==list[mid]:
    return True
  if value>=list[mid]:
    return binary_search(value,l[m+1:])
  else:
    return binary_search(value,l[:m])
