#"Given a string and an int n, remove characters from string starting from zero up to n and return a new string.
string = str(input("input the string:")) #Suggestion by Gopal = User input is string in default. No need to use type conversion.
num = int(input("input the num :"))
result = string[:num] #Does not satisfy question.
print(result)

#Given a list of ints, return True if first and last number of a list is same.
def return_true():
    l = [14,15,9,81,17,14]
    first = l[0]
    last = l[-1]
    if first == last :
        print("true")
    else:
        print("false")

return_true()        