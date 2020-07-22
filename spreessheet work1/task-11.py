#calculate the hypotenus of right angled triangle
from math import sqrt
p = int(input("input perpendicular:"))
b = int(input("input base :"))
h = sqrt(p**2 + b**2)
print("hypotenus is",h)
