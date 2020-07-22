#Write a function that returns the maximum of two numbers.
def maximum(a,b):
    if a > b:
        print("The number a is greater i.e :",a)
    else: 
        print("The number b is greater i.e :",b)
a = input("Input number a :")
b = input("Input number b :")
maximum(a,b)

#Write a function called fizz_buzz that takes a number.
#If the number is divisible by 3, it should return “Fizz”.
#If it is divisible by 5, it should return “Buzz”.
#If it is divisible by both 3 and 5, it should return “FizzBuzz”.
#Otherwise, it should return the same number.

def fizz_buzz(num):
    if num % 5 == 0 and num % 3 == 0: 
        print("FizzBuzz")
    elif num % 3 == 0: 
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
num = int(input("Enter a number :"))
fizz_buzz(num)

##Write a function called showNumbers that takes a parameter called limit. It should print all the numbers 
# between 0 and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

def showNumbers(limit):
    for x in limit:
        if x % 2 == 0:
            print (x, "EVEN")
        else:
            print(x, "ODD")
n = int(input("Input Limit :"))
limit = range(n)
showNumbers(limit)
