#Sum of 2 numbers
length = int(input('enter the length of your array: '))
array=[0]*length
for i in range(0, length, 1):
    array[i] = int(input('enter element: '))
array.sort()
nbr = int(input('enter the number: '))
i=0
while(i<len(array)):
    if array[i] > nbr:
        array.remove(array[i])
    i+=1
for i in range(0,len(array),1):
    x = nbr - array[i]
    if x in array:
        print(f"{x} + {array[i]} = {nbr}")
