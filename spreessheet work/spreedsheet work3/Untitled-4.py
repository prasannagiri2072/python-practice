#Exercise Question 4: arrange String characters such that lowercase letters should come first


inputStr = "PyNaTive"
lower = [] 
upper = []
for char in inputStr:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sortedString = ''.join(lower + upper)
print("the required new string is ", sortedString)

