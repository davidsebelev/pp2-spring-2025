#we can combine 
age = 36
txt = "My name is John, I am " + age
print(txt)

#to make it easier we use f 
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#A placeholder can include a modifier to format the value.
#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 zeros after the .
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#result 
#The price is 59.00 dollars


#Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)