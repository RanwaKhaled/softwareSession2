#Quick sort
# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]
  piv_index = low - 1
  
  for j in range(low, high):
    if array[j] <= pivot:
      piv_index = piv_index + 1
      (array[piv_index], array[j]) = (array[j], array[piv_index])

 
  (array[piv_index + 1], array[high]) = (array[high], array[piv_index + 1])

  return piv_index + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    pi = partition(array, low, high)

    # on the left of pivot
    quickSort(array, low, pi - 1)

    # on the right of pivot
    quickSort(array, pi + 1, high)

list =[15,19,9,25,1,3,29,11]

print('unsorted array: ', list)
quickSort(list,0,len(list)-1)
print('sorted array: ', list)
