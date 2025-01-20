#upper() returns all in upper
a = "Hello, World!"
print(a.upper())

#lower() returns all in lowercase
a = "Hello, World!"
print(a.lower())

#strip() removes all spaces
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#the replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method returns a list where the text between the specified separator becomes the list items.

#The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']