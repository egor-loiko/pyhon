# 4	Найти значение минимального элемента списка.
import random

n = int(input("Введите длину списка: \n"))
A = [random.randint(0, 99) for i in range(n)]

min = A[0]
max = A[0]
print(A)

for i in range(len(A)):
    if A[i] < min:
        min = A[i]
    if A[i] > max:
        max = A[i]

print("Минимальное значение списка = ", min)
print("Максимальное значение списка = ", max)
