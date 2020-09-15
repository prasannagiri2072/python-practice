#Given a number count the total number of digits in a number. 462973. 
# And get a list of multiplication of each number serially.
# For example: 4*6 = ?, 6*2 = ? and so on.

def serially():
    num = 4629973
    num0 = str(num)
    list1 = []
    a = 0
    for i in num0:
        n = int(i)
        product = a * n 
        a = n
        if product > 0:
            list1.append(product)
    print(list1)
serially()

