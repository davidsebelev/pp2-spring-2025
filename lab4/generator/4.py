def squares(a,b):
    for i in range(a, b+1):
        yield i * i


a, b =int(input()), int(input())
for values in squares(a,b):
    print(values)