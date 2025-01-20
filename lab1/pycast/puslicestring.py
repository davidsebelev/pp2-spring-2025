#Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5]) #res will be llo, 

#все до 5 индекса
b = "Hello, World!"
print(b[:5])

#all start from 2 to the end
#Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])

#neg index starting from -1 not 0 , 5 not including here
b = "Hello, World!"
print(b[-5:-2])