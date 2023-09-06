#Balanced brackets
brackets = input('enter your brackets ')
brackets = list(brackets)
i=0
while(i<len(brackets)):
    print(i)
    if brackets[i]=='(' :
        for j in range(i+1,len(brackets)):
            if brackets[j] == ')':
                brackets.remove(brackets[j])
                break

    print(brackets)
    i+=1

print(brackets)

if ')' in brackets:
    print('unbalanced')
else:
    print('balanced')
