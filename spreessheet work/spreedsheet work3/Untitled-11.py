#Given a following two sets find the intersection and remove those elements from the first set
#Expected Output:
#First Set  {65, 42, 78, 83, 23, 57, 29}
#Second Set  {67, 73, 43, 48, 83, 57, 29}
#Intersection is  {57, 83, 29}
#First Set after removing common element  {65, 42, 78, 23}

firstSet  = {23, 42, 65, 57, 78, 83, 29}
secondSet = {57, 83, 29, 67, 73, 43, 48}
intersection = firstSet.intersection(secondSet)
print("Intersection is ", intersection)
for x in intersection:
  firstSet.remove(x)

print("First Set after removing common element ", firstSet)

#spreedsheet work 3 Question no.19.
def check():
    firstSet  = {57, 83, 29}
    secondSet = {57, 83, 29, 67, 73, 43, 48}
    print("\n next function  output")
    print("The first set is subset of second set :",firstSet.issubset(secondSet))
    print("The second set is subset of first set :",secondSet.issubset(firstSet))

    print("The first set is superset of second set :",firstSet.issuperset(secondSet))
    print("The second set is superset of first set :",secondSet.issuperset(secondSet))
check()


    