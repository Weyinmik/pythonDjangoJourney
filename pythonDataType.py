"""
THINGS TO NOTE:
1. Every value in Python has a data type.
2. Everything is an object in Python programming.
3. Data types are classes. (Blue prints)
4. Variables are objects (any value stored in computer memory is an object) of classes.

7 DATA TYPES IN PYTHON
a. Numbers - whole numbers oof decimal numbers
b. Strings - ordered sequence of characters and written in single or double quotes.
c. List-written in square brackets []. Are ordered sequence of objects
d. Dictionaries - Unordered key value pairs. written in curly brackets {}
e. Tuples - ordered immutables sequence of objects. written in parenthesis ()
f. Sets - unordered collection of unique objects ("a", "b")
g. Logical values True of False
"""

# Strings and Indexing
# Indexing start with 0
# Anything you want to print as text should be in string
""" 
Indexing:           0   1   2   3   4
String  :           H   e   l   l   o
Reverse Indexing :  -5  -4  -3  -2  -1
"""
#1. String Concatenation
greeting ="Hello"
name = "Mark"
print(greeting + " " + name)

#2. String Input function
greeting ="Hello"
name = input("What is your name?")
print(greeting + " " + name)

#3a. Splitting of strings with \n (New line)
split_string = "Hello everyone, welcome to the world of python!!!"
print(split_string)
split_string = "Hello everyone, \nwelcome to the world of python!!!"
print(split_string)

#3a. Splitting of strings with \t (tab)
tab_split = "1\t2\t3\t4"
print(tab_split)
# Result of tab_split: 1    2   3   4

#4. String Indexing
colour = "orange"
len(colour) # The length of word orange = 6
print(colour[3])  # result is n. Index at position 3
print(colour[0])  # result is o. Index at postion 0
print(colour[-1]) # result is e. Reverse index at position -1
print(colour[-2]) # result is g.

#5. String Slicing
print(colour[0:3]) # result is ora. slicing from index 0 to 3. Upper bound 3 is excluded.
print(colour[0:4]) # result is oran. slicing from index 0 to 4. upper bound index 4 excluded.
print(colour[-4:-1]) # result is ang. upper bound of index postion -1 excluded.
print(colour[ :3]) # result is ora. slice from index 0 to 3 with 3 excluded. With space
print(colour[:3]) # result is ora. slice from the beginning of index 0 to 3 with 3 excluded. Without space
print(colour[2:]) # result is ange. slice from index 2 to the end.

#6. String Formatting
"""
Note: String and number cannot be concatinated together
Example:
age = 27
print("I am" + age + "year's old")
"""
#6a. Except the number is passed to a string with str. Example
age = str(27)
print("I am" + age + "Year's old.")
# Result: I am 27 Year's old.

#6b. OR
age = 27
print("I am" + str(age) + "Year's old.")
# Result: I am 27 Year's old.

#6c. OR
print("The colours are {} {} {}".format("Red","Green","Blue"))
#Result: The colours are Red Green Blue

#6d. OR
print("The colours are {0} {1} {2}".format("Red","Green","Blue"))
#Result: The colours are Red Green Blue

#6e. OR
print("The colours are {0} {0} {0}".format("Red","Green","Blue"))
#Result: The colours are Red Red Red

#6f. OR
print("The colours are {2} {2} {2}".format("Red","Green","Blue"))
#Result: The colours are Blue Blue Blue

#6g. OR
print("The colours are {r} {g} {b}".format(r="Red", g="Green", b="Blue"))
#Result: The colours are Red Green Blue

#6h. OR
print("The colours are {r} {r} {r}".format(r="Red", g="Green", b="Blue"))
#Result: The colours are Red Red Red

#6i.
pie = 3.14
print(pie)

print("The value of pie is {}".format(pie))
#Result: The value of pie is 3.14


