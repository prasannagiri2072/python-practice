s = [25,36,445,85,77,988,11,77,51,48,2,546,2323,44,22,55,2121]
r =[] 
for x in s:
    if x % 2 == 0 and x % 3 ==0 :
        print("even number is and number divisible by 3 is " , x)
        r.append(x)
print(r)

a = str(input("enter a word :"))
r = "".join(reversed(a))
print(r)

s = a[::-1]
print(s)


