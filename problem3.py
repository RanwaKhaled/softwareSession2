#Anagram:
str1=input('write the first string')
str2= input('write the second string')

str1 = list(str1)
str2 = list(str2)


str1.sort()
str2.sort()

if str1==str2:
    print('anagram')
else:
    print('not anagram')
