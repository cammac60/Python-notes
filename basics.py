# VARIABLES:
# No declaration
#ex:

first_var = "varibale"

# Multiple declarations on the same line:

second_var, third_var = 3, 4


#-------------------------------------------------------------------------------


# CONSOLE LOG/PRINT
# Print to the console using:

print("Insert a string or a var")
# Output: "Insert a string or a var"

print("multiple things seperated by commas", first_var)
# Output: "multiple things seperated by commas" "variable"


#-------------------------------------------------------------------------------


# CONCATINATION/PLACEHOLDERS
# A placeholder can be set using the % symbol followed by a letter in a string (%s for string, %d for num)
# Ex:

first_string = "%s is learning python"

# Print the string above and add in a word like so:

print(first_string%("Cameron"))

# Output: "Cameron is learning python"

# if a variable is being used the above example would change to:

name = "Cameron"
print(first_string%name)

# this can be done multiple times to the same string
# ex:

second_string = "%s is learning python version %d"

print(second_string%("Cameron", 3))


#-------------------------------------------------------------------------------


# LISTS/ARRAYS

# declare like so:

first_list = ["eggs", "milk", "coffee", "flour"]

# Accessed using bracket notation

print(first_list[0])

# Output: "eggs"

# Grab a portion of the array like so:

print(first_list[0:3])

# Output: ["eggs", "milk", "coffee"]

# First number represents starting point, second represents ending point. The end point will not be included in the return value so the example above grabs the items from index 0 to 2.

# Use the append method to add an item to the end of the array
# Ex:

first_list.append("grapes")

print(first_list)

# Output: ["eggs", "milk", "coffee", "flour", "grapes"]

# Use bracket notation to re-assign an index

# Ex:

first_list[0] = "kiwis"

print(first_list)

# Output:  ["kiwis", "milk", "coffee", "flour", "grapes"]

# To remove an item from the array, use the del method

# Ex:

del first_list[0]

print(first_list)

# Output: ["milk", "coffee", "flour", "grapes"]

# To see the amount of items in an array, use the len function

# Ex:

print(len(first_list))

# Output: 4

# To add two arrays together, simply use the + operator

# Ex:

second_list = ["bread", "cheese"]

print(first_list + second_list)

# Output: ["milk", "coffee", "flour", "grapes", "bread", "cheese"]

# Use the max and min fn to find the max and min of a list

# Ex:

number_list = [1, 44, 5, 87, 3]

print(max(number_list), min(number_list))

# Output: 87, 1


#-------------------------------------------------------------------------------


# OBJECTS/DICTIONARIES

# Var Ex:

students = {"Bob":34, "Tim":26, "Sarah":41}

# Access using bracket notation
# *If multiple keys have the same name, python will return the last one in the object when accessing

# Ex:

print(students["Bob"])

# Output: 34

# Re-assign:

students["Tim"] = 27

print(students["Tim"])

# Output: 27

# Removing Elements:

del students["Bob"]

print(students)

# Output: {"Tim":27, "Sarah":41}

# Find length:

print(len(students))

# Output: 2


#-------------------------------------------------------------------------------


# TUPLES

# The same as lists/arrays but immutable.

# Declaration:

first_tup = (1, 2, 3, 4, 5)

# Tuples can still be added together or spliced
# Tuples can still be deleted using the del method


#-------------------------------------------------------------------------------


# CONDITIONALS

# Ex:

if (5 > 3):
    print("true")

if (3 < 1):
    print("true")
else:
    print("false")

if (3 == 3):
    print("true")

# Output: true, false, true
# Use elif to add additional if statments
# and replaces &&
# or replaces ||

age = 25

if (age < 13):
    print("You can't see this PG-13 movie")
elif (age >= 13 and age < 18):
    print("You can see PG-13 but nor R")
else:
    print("You can see whatever you want")

# Output: "You can see whatever you want"


#-------------------------------------------------------------------------------


# FOR LOOPS:

list1 = ["apple", "orange", "cherry"]

for item in list1:
    print(item)

# Output: "apple", "orange", "cherry"

for i in range(0, 3):
    print(i)

# Output 0, 1, 2

# To increment by a certain amount, add an incementor as the third arg of orange

# Ex:

for i in range(0, 10, 2):
    print(i)

# Output: 0, 2, 4, 6, 8

# Can be nested:

for i in range(0, 10, 2):
    for j in range(0, 6):
        print(i -j)


#-------------------------------------------------------------------------------


# WHILE LOOPS

num = 3

while num <= 5:
    print(num)
    num = num + 1

# Output: 3, 4, 5

# Use break to end loop

num = 3

while num < 6:
    print(num)
    if (num == 4):
        break
    num = num + 1

# Use continue to stay in loop (In the example below, continue will skip on 3 and go back into the loop without running the print statement on the line below)

num = 0

while num < 6:
    num = num + 1
    if (num == 3):
        continue
    print(num)

# Output: 1, 2, 4, 5, 6
# Use pass as a filler statement. For example, if you know you need an if statement but aren't sure what needs to go inside of it yet.


#-------------------------------------------------------------------------------


# TRY/EXCEPT

# Operates the same as try and catch in JS

try:
    if undefined_var == 3:
        print("Hello")
except:
    print("The variable is undefined so we went into this block")


#-------------------------------------------------------------------------------


# FUNCTIONS
