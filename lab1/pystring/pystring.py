#you can use qoute in qoute but diff 

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


#You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#or
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#string its array so you can use index
#Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])

#also we can make use for with string
#loop through the letters in the word "banana":

for x in "banana":
  print(x)

#stirng length using len()

#to check phrase or character in a string use keyword in.

#Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)

#Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)
