# Modify elemement in following tuple.
# a = (10,20,30,40,50,90)
# Change it to (20,20,30,40,50,90)

a = (10,20,30,40,50,90)
b = list(a)
index = b.index(10)
b[index] = 20
c = tuple(b)
print(a)
