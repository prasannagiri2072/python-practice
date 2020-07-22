#Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters
#For Example: –
#sumAndAverage("English = 78 Science = 83 Math = 68 History = 65") = sum 294 Percentage is 73.5
def sum_and_average(English,Science,Math,History):
    sum = English + Science + Math + History
    percentage = sum/4
    print("sum =",sum,"percentage =",percentage)
(sum_and_average(78,83,68,65))



