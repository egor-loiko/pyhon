# 2.	Симметричная матрица.
# Дана квадратная матрица. Проверить, является ли она симметричной относительно главной диагонали.

import numpy as np
import random

n = int(input("Введите размерность матрицы: \n"))
A = np.array([[random.randint(1, 2) for j in range(n)] for i in range(n)])
print(A)
simIndicator = True
for i in range(n):
    if simIndicator:
        for j in range(n):
            if A[i][j] != A[j][i]:
                simIndicator = False
                break
    else:
        break
if simIndicator:
    print("Матрица симмметрична")
else:
    print("Матрица НЕ симмметрична")
