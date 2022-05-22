# 3.	Даны две квадратных таблицы чисел. 
# Требуется построить третью, каждый элемент которой равен сумме элементов, стоящих на том же месте в 1-й и 2-й таблицах.

import numpy as np
import random

n = int(input("Введите размерность квадратной таблицы чисел: \n"))
A = np.array([[random.randint(-5, 5) for j in range(n)] for i in range(n)])
B = np.array([[random.randint(-5, 5) for j in range(n)] for i in range(n)])
print("Таблица А")
print(A)
print("Таблица B")
print(B)
print("Таблица C")
print(A + B)
