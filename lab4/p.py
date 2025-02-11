lst = [1, 2, 3]
it = iter(lst)

print(next(it)) #1
print(next(it)) #2
print(next(it)) #3

#создаем класс
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value
    
for num in MyIterator(0, 5):
        print(num)