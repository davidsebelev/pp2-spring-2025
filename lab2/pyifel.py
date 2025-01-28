#if
a = 33
b = 200
if b > a:
  print("b is greater than a")

#If statement, without indentation (will raise an error):

a = 33
b = 200
#if b > a:
#print("b is greater than a") # you will get an error

#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#The else keyword catches anything which isn't caught by the preceding conditions

#a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#One line if statement:

if a > b: print("a is greater than b")

#One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")

#One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


#Test if a is NOT greater than b:

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
  