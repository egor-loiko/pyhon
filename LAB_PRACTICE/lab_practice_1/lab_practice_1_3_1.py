import random

# Все четные по значению элементы исходного списка A поместить в новый список B.

n = int(input("Введите длину списка: \n"))
A = [random.randint(0, 99) for i in range(n)]
B = []
print("Список А")
print(A)
for i in range(len(A)):
    if A[i] % 2 == 0:
        B.append(A[i])

print("\nСписок B")
print(B)
