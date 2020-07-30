# String characters balance Test
# We’ll say that a String s1 and s2 is balanced if all the chars in the string1 are there in s2. characters position doesn’t matter.
# For Example: 
# stringBalanceCheck(yn, Pynative) = True
def flag_statment(s1,s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag
s1 = "yn"
s2 = "Pynative"
flag = flag_statment(s1,s2)
print("s1 and s2 are balanced",flag)
s1 = "ynf"
s2 = "Pynative"
flag = flag_statment(s1,s2)
print("s1 and s2 are balanced",flag)


#Solution by Gopal
s1 = "h"
s2 = "hello"
if s1 in s2:
    print(f"{s1} is in {s2}. So it is balanced.")
else:
    print(f"{s1} is not in {s2}. So it is not balanced.")