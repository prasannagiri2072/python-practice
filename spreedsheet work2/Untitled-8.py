data = [15,-1,10,78,9]
l = 0 
s = 0
for num in data:
    if num > l:
        l = num
    elif num < s:
        s = num
print(l,s)

#Write a Python function that takes a positive integer and 
# returns the sum of the cube of all the positive integers smaller than the specified number.
def sum_of_cube(n):
    n = n - 1 
    total = 0
    while n > 0:
        total = total + n**3
        n = n - 1 
    return total 
print("sum of cubes:",sum_of_cube(8))      
