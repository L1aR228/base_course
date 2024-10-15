n = int(input("Введите число: "))
sp = []
for i in range(1, n):
    if sum(sp) == n:
        break
    else:
        if n % i == 0:
            sp.append(i)
print(*sp)