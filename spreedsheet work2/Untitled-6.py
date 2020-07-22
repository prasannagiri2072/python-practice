#Write a Python program to count the number 4 in a given list.
l = [15,6,17,4,5,4,12,4,5,6]
def count_num4(l):
    count = 0
    for x in l:
        if x ==4 :
            count = count + 1 
    return count
print("the num 4 in the list is :",count_num4(l))

#Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
def sum_num(a,b,c):
    if a == b == c :
        return (a+b+c)*3
    else:
        return a+b+c
print(sum_num(5,4,2))
print(sum_num(3,3,3))

#Write a Python program to remove the first item from a specified list.
l = ["apple","banana","coconut"]
l.pop(0)
print(l)
#or
p = ["apple","orange","coconut"]
del p[0]
print(p)




