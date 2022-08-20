from lib2to3.pgen2.token import NEWLINE


hello = "Hello"
name = input("What's your name?\n")
# \n = new line for the user to input value
# # creates comment
greeting = hello + " " + name
print(greeting)
