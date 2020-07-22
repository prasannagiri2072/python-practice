def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum

x = int(input("Input X :"))
y = int(input("Input Y:"))
print(sum(x, y))
