def s (numbers):
    new_list = []
    for i in range(len(numbers)-1):
        if numbers[i] != numbers[i+1]:
            new_list.append(numbers[i])
    if numbers:
            new_list.append(numbers[-1])

    return new_list

print(s([1,2,3,4,4,5,6,7,7]))