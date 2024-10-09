a = int(input('Первый член'))
b = int(input('знаменатель'))
c = int(input('количество'))
for i in range(c):
    step = a * (b ** i)
    print(step)
