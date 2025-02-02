def fu (numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] == 3 and numbers[i+1] == 3:
            return True
    return False
        
print(fu([1,2,3]))

