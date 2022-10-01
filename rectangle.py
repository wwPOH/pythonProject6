def read_rectangle(name: str) -> float:
    while True:
        x = input(f'{name}= ')
        try:
            x = float(x)
        except Exception:
            print('Это не число!')
            continue
        if x > 0:
            return x
        else:
            print('Это число не может быть стороной прямоугольника!')


def foursquare(a: float, b: float, c: float, d: float) -> float:
    if a == b == c == d:
        print("Это квадрат")


def does_rectangle_exist(a: float, b: float, c: float, d: float) -> bool:
    if a**2 + b**2 != c**2 + d**2:
        print("Выпуклый четырехугольник")
    elif a == c and b == d and a > b or a < b and a ** 2 + b ** 2 == c ** 2 + d ** 2:
        print("Это прямоугольник")
        return True
    else:
        print()
    return False


def rectangle_square(a: float, b: float, c: float, d: float) -> float:
    square = a * b
    return square

a = read_rectangle('a')
b = read_rectangle('b')
c = read_rectangle('c')
d = read_rectangle('d')
if foursquare(a, b, c, d):
    print()
elif does_rectangle_exist(a, b, c, d):
    print(f"Площадь прямоугольника: {rectangle_square(a, b, c, d)}")
else:
    print("Если вам нужен квадрат или прямоугольник,попробуйте еще и у вас всё получится ;)")