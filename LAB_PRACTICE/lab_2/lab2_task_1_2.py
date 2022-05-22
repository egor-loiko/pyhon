# 3 Найдите сумму отрицательных элементов списка.
# Найдите сумму элементов списка между двумя первыми нулями. Если двух нулей нет в списке, то выведите ноль.
import random

n = int(input("Введите длину списка: \n"))
A = [random.randint(-5, 5) for i in range(n)]

sum = 0
sumRange = 0
print(A)

for i in range(len(A)):
    if A[i] < 0:
        sum += A[i]

print("Сумма отрицательных чисел списка = ", sum)

try:
    firstIndex = A.index(0, 0, len(A))
    secondIndex = A.index(0, firstIndex + 1, len(A))
    for i in range(firstIndex + 1, secondIndex):
        sumRange += A[i]
    print("Сумма чисел между первыми двумя нулями = ", sumRange)
except ValueError:
    print("В списке не обнаружено двух нулей, сдедовательно сумма равна 0")
