#Write a Python program to accept a filename from the user and print the extension of that.
filename = "Abc.java"
f = filename.split(".")
print(f[-1])