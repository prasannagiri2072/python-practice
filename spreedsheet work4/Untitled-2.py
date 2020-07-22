#Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
#For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18.

def sum_of_mupltiples(limit):
    a = range(limit)
    s = 0
    p = 0
    for x in a:
        if x % 3 == 0:
            s+= x 
        elif x % 5 == 0 :
            p+= x
    print(s + p)
limit = int(input("Input the limit :"))
sum_of_mupltiples(limit)

#Write a function called show_stars(rows). If rows is 5, it should print the following:
def pyramid(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
pyramid(5)







