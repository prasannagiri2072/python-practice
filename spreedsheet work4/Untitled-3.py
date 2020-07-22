#Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.
def prime_numbers(limit):
    for x in range(0,limit + 1):
        if x > 1 :
            for y in range(2,x):
                if x % y == 0:
                    break
            else:
                print(x)
limit = int(input("Input the limit :"))
prime_numbers(limit)

##Iterate a given list and Check if a given element already exists in a dictionary as a key’s value if not delete it from the list
#Given:
#rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
#sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
#Expected Outcome: [47, 69, 76, 97]

rollNumber = [47,64,69,37,76,83,95,97]
sampleDict = {
    'Jhon': 47,
    'Emma': 69,
    'Kelly': 76,
    'Jason': 97
}
output = []
for i in sampleDict.values():
    if i in rollNumber:
        output.append(i)
print("NEW OUTPUT",output)







            