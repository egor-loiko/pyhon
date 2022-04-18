def is_sum_seven(n):
    A = list(str(n))
    temp = 0
    for i in range(len(A)):
        temp += int(A[i])
    if temp % 7 == 0:
        return True
    else:
        return False

for x in range(100000, 1000000):
    if is_sum_seven(x) and is_sum_seven(x + 1):
            print("Cумма цифр в числах " + str(x) + " и " + str(x + 1) + " делятся на 7")
