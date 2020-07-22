#Accept two int values from the user and return their product. If the product is greater than 1000, then return their sum.
def product_sum():
    a = int(input("input number a :"))
    b = int(input("input number b :"))
    product = a*b 
    if product > 1000:
        print(a + b)
    else:
        print(product)
product_sum()

#Accept string from the user and display only those characters which are present at an even index.
def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(odd_values_string('abcdef'))
print(odd_values_string('python'))
