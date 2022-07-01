def tribanachi_generator(val):
    trib1 = 0
    trib2 = 0
    trib3 = 1
    counter = 0
    while counter <= val:
        counter += 1
        if counter == 1 or counter == 2:
            yield trib1
        elif counter == 3:
            yield trib3
        else:
            sum_trib =  trib1 + trib2 + trib3
            trib1 = trib2
            trib2 = trib3
            trib3 = sum_trib
            yield sum_trib


element = int(input('Введите длину ряда трибоначчи: '))
tribananchi_iter = tribanachi_generator(element)

for i in tribananchi_iter:
    print(i)
