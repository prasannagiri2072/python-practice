n = 5
n2 = int("%s%s"%(n,n))
n3 = int("%s%s%s"%(n,n,n))
print("output is",n+n2+n3)

## spreed sheet task -2 Q.N- 6
def diff(n):
    if n <= 17 :
        return 17 - n 
    else:
        return (n - 17)*2 
print(diff(14))
print(diff(24))

