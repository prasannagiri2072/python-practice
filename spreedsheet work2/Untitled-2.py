# Write a Python program that will return true 
# if the two given integer values are equal or their sum or difference is 5.
def test_numbers(x , y):
    if x==y or abs(x-y)== 5 or (x+y)==5:
        return True 
    else:
        return False

print(test_numbers(7, 2))
print(test_numbers(3, 2))
print(test_numbers(2, 2))
print(test_numbers(9, 3))

#sorting the numbers in the descending order.
num = [15,14,24,18,9,7,12,16]
num.sort(reverse= True) 
print(num)