def fibonacci(n):
    cur = 0
    if n == 3:
        cur = 1
    if n > 3:
        cur = fibonacci(n - 1) + fibonacci(n - 2) + fibonacci(n - 3)
    return cur


element = int(input('Введите номер искомого элемента : '))
value = fibonacci(element)
print(str(element) + 'й элемент последовательности равен ' + str(value))

A = []
for i in range(element):
    A.append(fibonacci(i + 1))

print("Ряд трибоначи размером " + str(element) + " элементов\n", A)
