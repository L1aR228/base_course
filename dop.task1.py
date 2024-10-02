a = int(input())
b = int(input())
c = int(input())
s = 0
d = b ** 2 - 4 * a * c
if (((b*-1) + (0.5 * d)) / 2 * a) > 0:
    print('odin koren')
elif (((b*-1) - (0.5 * d)) / 2 * a) > 0:
    print('dva korna')

else:
    print('net korney')
#3х2- 5х+2=0