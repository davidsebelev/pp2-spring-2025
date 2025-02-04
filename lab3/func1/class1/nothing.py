class Cat:#класс
    def __init__(self, name, age, isHappy):# нужен чтобы создавать обьекты
        self.name = name
        self.age = age
        self.isHappy = isHappy

#обьекты
cat1 = Cat("Барсик", 3, True)
cat2 = Cat("Жепа", 3, False)

print(cat1.name)
print(cat2.name)