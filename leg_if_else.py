#else - условие - False
a = 3
if a > 4:
    print('hello 4')
else:
    print(f'hello {a}')

if a > 5:
    print('hello 5')
elif a < 2:
    print('hello 2')
else:
    print('aaa')