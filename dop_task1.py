num1 = int(input('число: '))
num2 = int(input('степень: '))


def stepen(a, n, count=1):
    for i in range(n):
        count *= a
    return count


print(stepen(num1, num2))