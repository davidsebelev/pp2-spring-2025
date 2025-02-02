def pali(word):
    new_word = "".join(reversed(word))
    return word == new_word
name = input()
print(pali(name))