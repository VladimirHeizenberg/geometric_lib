def area(a):
    """
    Возвращает площадь квадрата со стороной a

    Параметры:
        a(double): сторона квадрата

    Возвращаемое значение:
        S(double): площадь квадрата со стороной a
    """
    if a < 0:
        raise ValueError("Size of square cannot be negative!")

    return a * a


def perimeter(a):
    """
    Возвращает периметр квадрата со стороной a

    Параметры:
        a(double): сторона квадрата

    Возвращаемое значение:
        S(double): периметр квадрата со стороной a
    """
    if a < 0:
        raise ValueError("Size of square cannot be negative!")

    return 4 * a
