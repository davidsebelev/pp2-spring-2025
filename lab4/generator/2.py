def my_gen(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i
            


n = int(input())


result = ','.join(str(values) for values in my_gen(n))
print(result)