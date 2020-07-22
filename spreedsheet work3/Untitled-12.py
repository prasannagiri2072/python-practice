#Remove duplicate from a list and create a tuple and find the minimum and maximum number
#For Example:
#sampleList = [87, 45, 41, 65, 94, 41, 99, 94]

def max_min():
    sampleList = [87,45,41,65,94,41,99,94]
    uniqueList = list(set(sampleList))
    print(uniqueList)
    newlist = tuple(sampleList)
    print("max num =",max(newlist))
    print("min num =",min(newlist))
max_min()

