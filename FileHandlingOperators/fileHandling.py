## File Handling

# Read file from a default folder
my_file = open("dataTypeList.py")
my_file.read()                  #Result: It reads the content of the file as a string
my_file.read()                  #Result: '' It reads where the cursor is at the end of the file
my_file.seek(0)                 #Result: 0 - Takes the cursor to the beginning of the file
my_file.read()                  #Result: It reads the content of the file again from the beginning after seek(0)
my_file.seek(0)

my_file.readlines()             #Result: Read the file the way it is.
my_file.seek(0)

# Store file data into a variable
new_file = my_file.read()
new_file
new_file

# How to find the current directory.
pwd
        #Result:'C:\\Users\\koloh\\OneDrive\\Desktop\\pythonDjangoJourney'
# Read a file from anywhere in the computer
my_file = open("C:\\Users\\koloh\\OneDrive\\Desktop\\pythonDjangoJourney") # For Windows operating system
my_file.read() 
my_file.seek(0)
my_file.readlines() 

# For MAC/linux operating system
my_file = open("C:/Users/koloh/OneDrive/Desktop/pythonDjangoJourney")

# Close the file 
my_file.close() 

# If do not close an open file, we will not be able to edit, move the file from the computer     
            
