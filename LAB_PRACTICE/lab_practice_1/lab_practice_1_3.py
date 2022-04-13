import random

n = int(input("Введите диапазон: \n"))
A = [random.randint(0, 99) for i in range(n)]
B = []
print("Массив А")
for i in range(len(A)):
    print(str(i + 1) + 'й элемент = ' + str(A[i]))
    if A[i] % 2==0:
        B.append(A[i])


print("\nМассив B")
for i in range(len(B)):
    print(str(i + 1) + 'й элемент = ' + str(B[i]))
