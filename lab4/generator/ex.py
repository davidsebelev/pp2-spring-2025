#ex of gen

def my_gen():
    yield 1
    yield 2
    yield 3

for value in my_gen():#yield это значение в генераторе
    print(value)


    