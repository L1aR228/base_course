a = int(input())
b = int(input())
if b == 0:
    print('Ti che tvorish')
elif a % b == 0:
    print(f'Delitsa {a % b}')
else:
    print(f'Ne delitsa {a % b}')