a = int(input())
b = int(input())
c = int(input())
s = 0
d = b ** 2 - 4 * a * c
k1 = (((b*-1) + (0.5 * d)) / 2 * a)
k2 = (((b*-1) - (0.5 * d)) / 2 * a)

if k1 >= 0 or k2 >= 0:
    if k1 > 0 and k2 > 0:
        print('dwa koren', k1, k2)
    if k1 > 0 and k2 < 0:
        print('odin koren', k1)
    if k1 < 0 and k2 > 0:
        print('odin koren', k2)

else:
    print('net korney')
#3х2-6х = 0