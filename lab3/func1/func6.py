def returnReverse(s):
    sen = s.split()
    reversed_sen = " ".join(reversed(sen))
    return reversed_sen

s = input()
print(returnReverse(s))

