class stringManipulator:
    def __init__(self):
        self.text = "" #переменнная которая хранит строку

    def getString(self):
        self.text = input("Введи строку") #metod от пользователя получает строку и записывает

    def printString(self):
        print(self.text.upper())

obj = stringManipulator()
obj.getString()
obj.printString()
