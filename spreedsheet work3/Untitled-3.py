#Given a string of odd length greater 7, return a string made of the middle three chars of a given String.
# Example:
# getMiddleThreeChars("JhonDipPeta") → "Dip"
# getMiddleThreeChars("Jasonay") → "son"
def middle_char(txt):
   return txt[(len(txt)-2)//2:(len(txt)+3)//2]
print(middle_char("JhonDipPeta"))
print(middle_char("Jasonay"))
print(middle_char("jomsombaz"))


##Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1.
#Example:
#Input: "Chrisdem", IamNewString
#Output: "ChrIamNewStringisdem"
def add_strings():
   s1 = "Chrisdem"
   s2 = "IamNewString"
   New_string = s1[:3] + s2 + s1[3:]
   return New_string
print("The New String is :",add_strings())
#TODO: Make it possible for any string

#Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string.
#Example:
#Input: "America", "Japan"
#Ouput: "AJrpan"
strg1 = "America"
strg2 = "Japan"
a = strg1[3]
b = strg2[2] 
Newstring = strg1[0] + strg2[0] + a + b + strg1[-1] + strg2[-1]
print(Newstring)
#TODO: Make it possible for any string. Check for odd length before continue. Take user input.