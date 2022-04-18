#1	Ввести три числа m, n, p. Подсчитать количество отрицательных чисел.

A = [int(input("Введите первое число: \n")),
     int(input("Введите второе число: \n")),
     int(input("Введите третье число: \n"))]

for i in range(len(A)):
    print(str(i + 1) + "е число: " + str(A[i]))

count = 0
for x in range(len(A)):
    if A[x] < 0:
        count += 1

print("Количество отрицательных чисел: " + str(count))
