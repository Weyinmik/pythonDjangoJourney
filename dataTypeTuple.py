"""
Ordered immutable sequence of objects
("Hello", 100,24,7)

It is very similar to list but cannot be changed or modified
"""
#1. Define a Tuple
prime_numbers = (2,3,5,7,11)
type(prime_numbers)                 #Result: Tuple
my_tuple = ("Hello", 100,24.7)
print(my_tuple)

#2. Indexing in Tuple
my_tuple[0]                         #Result: 'Hello'
my_tuple.count(100)                 #Result: 1
my_tuple[-1]                         #Result: 24.7 

#3. Difference between the List and Tuple.
l = ["a","b","c","d","e"]     
t = ("a","b","c","d","e")
type(l)                             #Result: list
type(t)                             #Result: tuple