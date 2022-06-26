class TribanachiIterator:
    trib1 = 0
    trib2 = 0
    trib3 = 1

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            if self.counter == 1 or self.counter == 2:
                return self.trib1
            elif self.counter == 3:
                return self.trib3
            else:
                sum_trib =  self.trib1 + self.trib2 + self.trib3
                self.trib1 = self.trib2
                self.trib2 = self.trib3
                self.trib3 = sum_trib
                return sum_trib
        else:
            raise StopIteration

    def __iter__(self):
        return self

element = int(input('Введите длину ряда трибоначчи: '))
tribananchi_iter = TribanachiIterator(element)

for i in tribananchi_iter:
    print(i)
