
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
print("s! and s2 are balanced",flag)
