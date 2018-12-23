"""
Dictionaries in Python are unordered key value pairs
{"key1":"value1","key2":"value2"}
"""
"""
WHEN TO USE DICTIONARY AND LIST
1. Dictionary:
Objects are retrieved by its key name
You can quickly retrieve the value by its key name without needing to know the index location.

2. List:
objects in list are retrieved by its index location.
it is easy to perform an operation on the basis of index location
"""
#1. Define  Dictionary
my_dict = {"key1":"value1","key2":"value2"}
print(my_dict)
print(my_dict["key1"])

fruits = {"Apple":3, "Banana":1.75, "Cherry":2}
print(fruits)


#2. Dictionaries with all data types
new_dict = {"k1":147, "k2": [15,25,35], "k3":{"Apple":3}}
print(new_dict)
print(new_dict["k2"])           #Result: [15,25,35]
print(new_dict["k2"][1])        #Result: 25
print(new_dict["k3"])           #Result:{'Apple':3}
print(new_dict["k3"]["Apple"])           #Result: 3

d = {"students":["a","b","c","d"]}
print(d)                        #Result: ['a','b','c','d']
print(d["students"][1])         #Result: 'b'
print(d["students"][1]).upper()         #Result: 'B'
print(d["students"][1]).lower()         #Result: 'b'

#3. Add values
dict = {"k4":100, "k5":200}
print(dict)
dict["k6"] = 300
print(dict)                     #Result: {'k4':100, 'k5':200, 'k6':300}

#4. Replace Values
dict["k4"] = "New ONe"
print(dict)                     #Result: {'k4':'New One', 'k5':200, 'k6':300}

#5. Keys, Values and Items retrieval
print(dict.keys())              #Result: Print out all the keys in the dictionary dict, dict_keys(['k4', 'k5', 'k6'])
print(dict.values())              #Result: Print out all the values in the dictionary dict, dict_values([100, 200, 300])
print(dict.items())              #Result: Print out all the items in the dictionary dict in tuple form, dict_items([('k4', 100), ('k5', 200), ('k6', 300)])