def test_numbers(x , y):
    if x==y or abs(x-y)== 5 or (x+y)==5:
        return True 
    else:
        return False

print(test_numbers(7, 2))
print(test_numbers(3, 2))
print(test_numbers(2, 2))

num = [15,14,24,18,9,7,12,16]
num.sort(reverse= True) 
print(num)