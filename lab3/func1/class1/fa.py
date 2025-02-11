def fact(x):
    sum = 1
    for i in range(1,x+1):
        sum = sum *i
    return sum
print(fact(5))