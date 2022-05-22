# 1.	В матрице найти номер строки, сумма чисел в которой максимальна.
import random

import numpy as np

n = int(input("Введите количество строк массива: \n"))
m = int(input("Введите количество столбцов массива: \n"))
A = np.array([[random.randint(-5, 5) for j in range(m)] for i in range(n)])
print(A)
sum = tempSum = maxIndex = 0
for i in range(n):
    for j in range(m):
        tempSum += A[i][j]
    print(tempSum)
    if tempSum > sum:
        sum = tempSum
        maxIndex = i
print("Номер строки с максимальной суммой чисел = ", maxIndex+1)
