a = int(input('первая сторона: '))
b = int(input('вторая сторона: '))
c = int(input('третья сторона: '))
if a + b > c and b + c > a and c + a > b:
    if a == b and b == c and c == a:
        print('Равносторонний')
    elif a != b and b != c and c != a:
        print('Разносторонним')
    elif a == b or b == c or c == a:
        print('Равнобедренный')
else:
    print('Такого треугольника не существует')
    print('my name Gustao but you can call me SAS')