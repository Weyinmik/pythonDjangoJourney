"""
This is unordered collection of unique and immutable objects.
("a", "b") -always defined in parenthesis.
When same objects are entered multiple times, it will take only one type of that object
"""
#Set definition
my_set = set()
print(my_set)                   #Result: ([])

my_set.add("Hello")
print(my_set)                   #Result: (['Hello'])

my_set.add(24)
print(my_set)                   #Result: ([24, 'Hello'])

my_set.add("Hello")
print(my_set)                   #Result: ([24, 'Hello']). Note that Hello is not repeated twice.

# TO SHOW THE DIFFERENCE BETWEEN SET AND LIST
my_list = [1,1,1,2,2,3,"Apple","Apple"]
print(my_list)                  #Result: [1,1,1,2,2,3,"Apple","Apple"]
print(set(my_list))             #Result: ([1,2,3,'Apple'])

