def area(a, b):
    """
    Возвращает площадь прямоугольника со сторонами a и b

    Параметры:
        a(double): 1-ая сторона прямоугольника
        b(double): 2-ая сторона прямоугольника

    Возвращаемое значение:
        S(double): площадь прямоугольника со сторонами a и b
    """
    if a < 0:
        raise ValueError("Size of reactangle cannot be negative!")

    if b < 0:
        raise ValueError("Size of reactangle cannot be negative!")

    return a * b


def perimeter(a, b):
    """
    Возвращает периметр прямоугольника со сторонами a и b

    Параметры:
        a(double): 1-ая сторона прямоугольника
        b(double): 2-ая сторона прямоугольника

    Возвращаемое значение:
        P(double): периметр прямоугольника со сторонами a и b
    """
    if a < 0:
        raise ValueError("Size of reactangle cannot be negative!")

    if b < 0:
        raise ValueError("Size of reactangle cannot be negative!")

    if a == 0:
        return b

    if b == 0:
        return a

    return 2 * (a + b)
