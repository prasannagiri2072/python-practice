#Find all occurrences of “USA” in given string ignoring the case
#Expected Outcome:
#input_str = "Welcome to USA. usa awesome, isn't it?"
#The USA count is: 2
def occurrences(new_string):
    low = new_string.lower()
    sub_string = "usa"
    count = low.count(sub_string)
    return count
new_string = "Welcome to USA. usa awesome, isn't it?"
print("the occurrences of usa in the statment is", occurrences(new_string))



        