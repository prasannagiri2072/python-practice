##Given a list of numbers, Iterate it and print only those numbers which are divisible of 5.
def divisible():
    l = [14,25,40,77,6,5,14,48,98,100,75,84,95,71,60]
    s =[]
    for x in l:
        if x % 5 == 0:
            s.append(x)
    return s 
print(divisible())               

n = int(input("input integer:"))
string = str(n)
lst = list(string)
lst.reverse()
string = "".join(lst)
string = int(string)
if string == n :
    print ("the revese is same ")
else:
    print(" No! reverse is differnt ")




