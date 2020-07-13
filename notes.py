# VARIABLES:
# No declaration
#ex:

first_var = "varibale"

# Multiple declarations on the same line:

second_var, third_var = 3, 4

#-------------------------------------------

# CONSOLE LOG/PRINT
# Print to the console using:

print("Insert a string or a var")
# Output: "Insert a string or a var"

print("multiple things seperated by commas", first_var)
# Output: "multiple things seperated by commas" "variable"

#-------------------------------------------

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

#-------------------------------------------

# LISTS/ARRAYS

# declare like so:

first_list = ["eggs", "milk", "coffee", "flour"]

# Accessed using bracket notation

print(first_list[0])

# Output: "eggs"
