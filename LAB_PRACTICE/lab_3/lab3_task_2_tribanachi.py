def tribonacci(n):
    cur = 0
    if n == 3:
        cur = 1
    if n > 3:
        cur = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
    return cur


element = int(input('Введите длину ряда трибоначчи (желательно не более 30) : '))
if element > 30:
    print("Слишком длинный ряд, вычисление займет много времени")
else:
    value = tribonacci(element)
    print(str(element) + 'й элемент последовательности равен ' + str(value))

    A = []
    for i in range(element):
        A.append(tribonacci(i + 1))

    print("Ряд трибоначи размером " + str(element) + " элементов\n", A)
