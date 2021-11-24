# Syntax :  Variable name = data
# data type is not used as prefix while initializing a variable
# since python is dynamically typed language a variable can have any value during run-time.

a=10                        # Assignment of value to variables
print(a , "=", type(a))     # Integer variable  
a=10.5      
print(a, "=", type(a))      # Float Variable
a="hello"   
print(a, "=", type(a))      # String variable

# Multiple variable initialization
a, b, c = 50, 50.55, "Hello world"
print(a, b, c)
a = b = c = 50               # Assigning a value to multiple variables
print(a, b ,c)