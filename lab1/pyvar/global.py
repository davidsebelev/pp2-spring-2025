#global var vars that made outside the func
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


x = "awesome"#global

def myfunc():
  x = "fantastic" #local
  print("Python is " + x)

myfunc()

print("Python is " + x)

#To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)