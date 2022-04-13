# m = int(input("Введите первое число: \n"))
# n = int(input("Введите второе число: \n"))
# p = int(input("Введите третье число: \n"))

A = []
A.append(int(input("Введите первое число: \n")))
A.append(int(input("Введите второе число: \n")))
A.append(int(input("Введите третье число: \n")))

for i in range(len(A)):
    print(str(i + 1) + "е число: " + str(A[i]))

count = 0
for x in range(len(A)):
    if A[x] < 0:
        count += 1

print("Количество нечетных чисел: " + str(count))
