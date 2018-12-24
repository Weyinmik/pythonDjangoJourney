"""
LOOPS ...FOR, WHILE

For Loop!
Used to iterate over elements of a sequence.

When you have a piece of code which you want to repeat "n" number of times

While Loop!
Used to iterate over a block of code as long as condition is true

Terms: Pass Continue Break
"""
#For Loop
my_list = [1,2,3,4,5,6,7,8,9,10]

for num in my_list:
    print(num)

for num in my_list:
    if num % 2 == 0:
        print(num)

for num in my_list:
    if num % 2 != 0:
        print(num)

# Example2
your_list = [1,2,3,4,5]
list_sum = 0

for num in your_list:
    list_sum = list_sum + num
print(list_sum)                 #Result:15 

# For loop for string
 
my_string = "Hello World" 
for letters in my_string:
    print(letters)

for i in "string":
    print(i) 

# For loop with tuples
my_list = [(1,2), (3,4), (5,6), (7,8)]
print(len(my_list))

for tup in my_list:
    print(tup)

# Print pair of items in list of tuple - 1 2,3 4,5 6,7 8
for a,b in my_list:
    print(a,b)

# Print first item in every tuple - 1,3,5,7
for a,b in my_list:
    print(a)

# Print second item in every tuple - 2,4,6,8
for a,b in my_list:
    print(b)

my_list = [(1,2,3),(4,5,6),(7,8,9)]

# To print 1,4,7
for a,b,c in my_list:
    print(a)

# To print 2,5,8
for a,b,c in my_list:
    print(b)

# To print 3,6,9
for a,b,c in my_list:
    print(c)

# To print 2 3,5 6,8 9
for a,b,c in my_list:
    print(b,c)

# For loop with dictionary
my_dict = {"k1":1, "k2":2, "k3":3}

# To print out  only keys in the output - k1,k2, k3
for i in my_dict:
    print(i)


# To print out keys and corresponding values in the output - ('k1',1),('k2',2), ('k3',3)
for i in my_dict.items:
    print(i)

# To print out  only values in the output - 1,2,3
for a,b in my_dict:
    print(b)


# While Loop
i = 0
#while i < 5: 
    #print(i)            # This result in never ending loop. The program keep running


# Print out 0,1,2,3,4
i = 0
while i < 5: 
    print(i)
    i = i + 1 

# Print out 0,1,2,3,4, 'i is not less than 5'
i = 0
while i < 5: 
    print(i)
    i = i + 1 
else:
    print("i is not less than 5")


# Print out 'i is not less than 5'
i = 10
while i < 5: 
    print(i)
    i = i + 1 
else:
    print("i is not less than 5")


# Pass Break Continue
l = [1,2,3,4,5]
for items in l:
    #pass
    pass            # We simply pass the program to next line
print("I will work after!!!")

#Break
# print out : H e l l o W o
my_string = "Hello World"
for letters in my_string:
    if letters == "r":
        break
    print(letters)

# continue
# print out : H l l o W o l d
my_string = "Hello World"
for letters in my_string:
    if letters == "e":
        continue
    print(letters)

# Print out 0,1,2,3,4
i = 0
while i < 5: 
    if i == 3:
        break
    print(i)
    i = i + 1 
