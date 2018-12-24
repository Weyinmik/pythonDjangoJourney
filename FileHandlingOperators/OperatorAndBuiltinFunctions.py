#  OPERATORS AND BUILT IN FUNCTIONS

# Cpmparison Operator in Python

print(5 == 5)           #Result: True

print(5 == 7)           #Result: False

print("Hello"== "Hello")           #Result: True

print("Hello"== "Bye")           #Result: False

print("Hie"== "hie")           #Result: False

print(7 != 5)                  #Result: True

print(7 > 5)                  #Result: True

print(12 >= 10)                  #Result: True

# Logical operators
print(3 > 2> 1)             #Result: True

print(3 > 2 and 2 > 1)             #Result: True

print(3 > 2 and 2 < 1)             #Result: False

print(3 > 2 or 2 > 1)             #Result: True

print(5>3)             #Result: True
print(not(5>3))             #Result: False

# BUILT IN FUNCTIONS

# print function
#python 3.6 has 68 built in functions
print(dir(__builtins__))        #Result: Shows the 68 Built in functions

print(pow(2,3))                 #Result: 8 - 2 into power 3.

a = (10,20,30,40,50)
b = "Hello"
max(a)                          #Result: 50
min(a)                          #Result: 10
len(b)                          #Result: 5