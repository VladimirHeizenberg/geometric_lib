import math


def area(r):
    """
    Возвращает площадь круга радиусом r

    Параметры:
        r(double): радиус круга

    Возвращаемое значение:
        S(double): площадь круга радиусом r
    """
    if r < 0:
        raise ValueError('R cannot be negative!')

    return math.pi * r * r


def perimeter(r):
    """
    Возвращает периметр круга радиусом r

    Параметры:
        r(double): радиус круга

    Возвращаемое значение: длина окружности радиуса r
    """
    if r < 0:
        raise ValueError('R cannot be negative!')

    return 2 * math.pi * r
