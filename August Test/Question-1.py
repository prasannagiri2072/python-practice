#Access value 20 from following tuple.
#a = ("Mango", (10,20,30), [52,63,41], "Cherry")

a = ("Mango", (10,20,30), [52,63,41], "Cherry")
for x in a:
    if x == (10,20,30):
        p = x 
for i in p:
    if i == 20:
        print(f"the item {i} is access form the tuple")

#or by this method
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])