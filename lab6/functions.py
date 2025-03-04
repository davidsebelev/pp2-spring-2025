#1
import math 

def multiplu(nums):
    return math.prod(nums)

lit = [1,3,3]
print(multiplu(lit))


#2
def count_l(word):
    count_up = 0
    count_low = 0
    for i in word:
        if word.isupper():
            count_up +=1
        elif word.islower():
            count_low +=1
    return count_up,count_low


print(count_l("aboba"))

#3
def pali(word):
    w = word.lower()
    return w == w[::-1]

print(pali("lol"))
    
#4

import math
import time

def delayed_square(number,delay_ms):
    time.sleep(delay_ms/1000.0)
    sqrt_value = math.sqrt(number)
    return sqrt_value

number = float(input())
delay_ms = float(input())

print(number,delay_ms,delayed_square(number,delay_ms))

#5
def all_true(t):
    return all(t)
print(all_true(True,1,"hello"))