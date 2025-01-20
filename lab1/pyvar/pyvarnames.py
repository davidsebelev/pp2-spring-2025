#some rules for py names
#1.starts from letter or _
#2.no start form number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#A variable name cannot be any of the Python keywords.

#legal names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#not legal names
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""

#Variable names with more than one word can be difficult to read.
#There are several techniques you can use to make them more readable:

#camel case where all letter except the first is upper 
myVariableName = "John"

#pascal case all letter is upper im talking about first not all as i wrote
MyVariableName = "John"

#snake case each word separated by _
my_variable_name = "John"