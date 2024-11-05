word = input('выберите фигуру: ')


def kvadrat():
    s = int(input('сторона: '))
    return f'Площадь квадрата равна {s ** 2}'


def pramoygolnik():
    a = int(input('первая сторона: '))
    b = int(input('вторая сторона: '))
    return f'Площадь прямоугольника равна {a * b}'


def tereug():
    a = int(input('основание: '))
    h = int(input('высота: '))
    return f'Площадь треугольника ровна {0.5 * a * h}'


def kryg():
    r = int(input('радиус: '))
    return f'Площадь круга равна {3.14 * (r ** 2)}'


if word == 'квадрат':
    print(kvadrat())
if word == 'прямоугольник':
    print(pramoygolnik())
if word == 'треугольник':
    print(tereug())
if word == 'круг':
    print(kryg())