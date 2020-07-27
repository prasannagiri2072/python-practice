#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 

n = 5
n2 = int("%s%s"%(n,n))
n3 = int("%s%s%s"%(n,n,n))
print("output is",n+n2+n3)

#Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference.
def diff(n):
    if n <= 17 :
        return 17 - n 
    else:
        return (n - 17)*2 
print(diff(14))
print(diff(24))

