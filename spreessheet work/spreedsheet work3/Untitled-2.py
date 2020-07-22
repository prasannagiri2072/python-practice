##Given a two list of ints create a third list such that should contain only odd numbers from 
# the first list and even numbers from the second list.
#Example: 
#listOne = [10, 20, 23, 11, 17]
#listTwo = [13, 43, 24, 36, 12]
#Merged List is
#[23, 11, 17, 24, 36, 12]
def Merge_list():
    listOne = [10,20,23,11,17]
    listTwo = [13,43,24,36,12]
    s = []
    for x in listOne:
        if x % 2 == 1:
            s.append(x)
    for y in listTwo:
        if y % 2 == 0:
            s.append(y)
    print(s)
Merge_list()    
