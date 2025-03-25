def fact(x):
    sum = 1
    for i in range(1,x+1):
        sum = sum *i
    return sum
print(fact(5))


#int float and bool are inmutuable because
#so if we want to change some object for ex:

a = 10
#we nedd to make new a

#if we make tuple 
a =(1,2,3)
#we cant change but

list = [1,23,4]

list.append(6)

#also if list was empty we can append smth
a = []
a.append(78)