#Write a Python program to check if multiple variables have the same value.
x = 20
y = 20
z = 20
if x == y == z == 20:
    print("All variables have same value!")  

##Write a Python function to find the maximum and minimum numbers from a sequence of numbers. 
def max_min(data):
  l = 0
  s = 0
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))



