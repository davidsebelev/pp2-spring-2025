print(10>9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33
if b > a:
    print("b is greater")
else:
    print("b is not greater")


print(bool("hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#following return true

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")