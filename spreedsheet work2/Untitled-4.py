

#input the comma seprated numbers form the user and display the numbers in the list.
def create_list():
    l = values.split(",")
    t = tuple(l)
    print('List : ',l)
    print('Tuple : ',t)
    
values = input("Input some coma seprated numbers :")
create_list()

