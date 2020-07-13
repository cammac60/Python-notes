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
