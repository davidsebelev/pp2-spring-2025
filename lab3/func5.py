import itertools


def returnPerm(word):
    return itertools.permutations(word)

word = input()
per = returnPerm(word)
for i in per:
    print("".join(i))
