#Given a string input Count all lower case, upper case, digits, and special symbols.
#Example: 
#Input_str = "P@#yn26at^&i5ve"
#Total counts of chars, digits,and symbols Chars = 8 Digits = 3 Symbol = 4

Input_str = "P@#yn26at^&i5ve"
words = Input_str.split() #TODO: Why is this?
lower = 0
upper = 0    
digits = 0
symbol = 0 
for char in Input_str:
    if char.islower():
        lower += 1 
    elif char.isupper():
        upper += 1 
    elif char.isnumeric():
        digits += 1
    else:
        symbol += 1 
print("lower =",lower,"upper =",upper,"digits =","symbols =",symbol)


#TODO: Try to use dictionary to get the count.