def area(a, h):
    """
    Возвращает площадь треугольника со стороной a и высотой h,
    проведённой к этой стороне

    Параметры:
        a(double): сторона
        h(double): высота

    Возвращаемое значение:
        S(double): площадь треугольника
    """
    if a < 0:
        raise ValueError('Size of triangle cannot be negative!')

    if h < 0:
        raise ValueError('Height of triangle cannot be negative!')

    return a * h / 2


def perimeter(a, b, c):
    """
    Возвращает периметр треугольника со сторонами a, b, c

    Параметры:
        a(double): 1-ая сторона треугольника
        b(double): 2-ая сторона треугольника
        c(double): 3-я сторона треугольника

    Возвращаемое значение:
        P(double): периметр треугольника
    """
    if a < 0 or b < 0 or c < 0:
        raise ValueError('Size of triangle cannot be negative!')

    if a + b < c or b + c < a or a + c < b:
        raise ValueError('Triangle enaquality is not kept')

    return a + b + c
