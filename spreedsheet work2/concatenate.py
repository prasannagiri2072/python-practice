def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result
elements = ["Hello", "world.", "I", "am", "here", "to", "learn", "Python."]
result = concatenate_list_data(elements)
print(result)


#Solution by Gopal
def join_elements(list):
    return " ".join(list)

elements = ["Hello", "world.", "I", "am", "here", "to", "learn", "Python."]
result = join_elements(elements)
print(result)
