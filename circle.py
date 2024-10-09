import math


def area(r):
    '''
    Возвращает площадь круга радиусом r
    
    Параметры:
        r(double): радиус круга

    Возвращаемое значение:
        S(double): площадь круга радиусом r
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга радиусом r
    
    Параметры:
        r(double): радиус круга

    Возвращаемое значение: длина окружности радиуса r
    '''
    return 2 * math.pi * r

