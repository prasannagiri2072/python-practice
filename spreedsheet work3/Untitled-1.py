#Display the multiplication table from 2 to 5.
n = range(2,6)
s = range(1,6)
for x in n:
    for z in s:
        print(x,"*",z,"=",x*z)

#Given a list of numbers. Iterate over all the numbers, 
# divide all of them by 5 and save the answers (float value) in a list with ascending order.
l = [42,15,189,14,54,65,74,13,19]
m = []
for x in l:
    o = x/5
    m.append(o)
print(m)

