#Binary search recursion
#Recursive method
def binary_search_r(list, start, end, nbr):
    list.sort()
    if end>=start:
      middle = start+int((end-start)/2)
      if nbr == list[middle]:
        return f'found'
      elif nbr>list[middle]:
        return binary_search_r(list, (middle+1), end, nbr)
      else:
        return binary_search_r(list,start,(middle-1), nbr)
    else:
        return 'not found'
list =[15,19,9,25,1,3,29,11]
print(binary_search_r(list,0,len(list)-1, 3))
print(binary_search_r(list,0, len(list)-1, 25))
print(binary_search_r(list,0, len(list)-1, 5))
