num = int(input("Input a four digit numbers: "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)


#Solution by Gopal
n = input("Input a four digit numbers: ")
n1 = int(n[0])
n2 = int(n[1])
n3 = int(n[2])
n4 = int(n[3])

print(f"The sum of digits in the number is {n1+n2+n3+n4}.")