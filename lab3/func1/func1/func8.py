def check(numbers):
    pattern = [0,0,7]
    count = 0

    for num in numbers:
        if num == pattern[count]:
            count+=1
        if count == len(pattern):
            return True
    
    return False

print(check([0,0,7,1,2,3]))