"""
List is ordered sequence of objects - That is, it follows a particular order;
It is mutable - can be changed or  modified.
It is always in square bracts[] and objects in the list are seperated with comma.
It can contain all data types- ["Hello", 213, 54,6,("a","b")]

"""
#1a. List Definition and Print.
my_list = ["Hello", 100, 23.47]
print(my_list)

second_list = ["one", "two", "three"]
print(second_list)

print(my_list, second_list)     #The 2 list are printed on thesame line because of the comma(,). Result:['Hello', 100, 23.47] ['one', 'two', 'three']

#1b. List Concatenation with +
new_list = my_list + second_list
print(new_list)     #Result:["Hello", 100, 23.47, "one", "two", "three"] 

#2. Define Empty List
empty_list = []
print(empty_list)       #Result: []. 
#Why define empty list. Because list are mutable we can always add objects to and empty list.

#3. List Indexing and Slicing works the same as indexing in string data type
students = ["Robert", "Chris", "Katrina", "Scarlet"]
print(students)     # Or you can type in just students to print the list stored in the variable students.
students[0]         #Result: 'Robert'
students[-1]        #Result: 'Scarlet'
students[0:2]       #Result: 'Robert','Chris'


#4. Editing the list's (Deleting,Replacing objects in the list)

#Replacing the values in the list with index
students[0] = "Sam"     # Replaces Robert with Sam
students                # Result: 'Sam','Chris','Katrina','Scarlet'

#Add values to list by append function.
students.append("Paul")
students                #Result: 'Sam','Chris','Katrina','Scarlet','Paul'

#Remove Items from the list with remove function
students.remove("Scarlet")      # Delete Scarlet from the list.
students                        #Result: 'Sam','Chris','Katrina','Paul' 

# Remove with pop() function. Another method of removing from the list.
list1 = ["one","two","three","four","five"]
list1
list1.pop()         # Remove the last item from the list - 'five'
list1.pop(0)        # Remove the item of index 0 from the list1 -'one'

#5. Add list into list
color = ["Red","Green","Blue","Violet"]
color
age = [21,23,25,27]
age

# Add list into list with extend() function.
color.extend(age)
color               #Result: ['Red','Green','Blue','Violet',21,23,25,27]


#6. Python in-built functions with the list's.
even = [2,4,6,8]
odd = [1,3,5,7,9]
numbers = even + odd
numbers       #Result: [2,4,6,8,1,3,5,7,9] - Note that the numbers are not sorted

# Sort the number list with the sorted() function.
print(sorted(numbers))         #Result: [1,2,3,4,5,6,7,8,9]

len(numbers)        #Result: 9 - The lenth of the numbers list
max(numbers)        #Result: 9 - The largest number in the numbers list
min(numbers)        #Result: 1 - The smallest number in the numbers list.
