def rectangleCount(a, b):
    if a == b:
        count = 1
    else:
        count = rectangleCount(max(a, b) - min(a, b), min(a, b)) + 1
    return count


a = int(input('Введите длину стороны a : '))
b = int(input('Введите длину стороны b : '))
print('Количество квадратов которые можно вписать в прямоугольник со сторонами ' + str(a) + ' и ' + str(
    b) + ' равно: ' + str(rectangleCount(a, b)))
