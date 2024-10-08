def area(a, h): 
    '''
    Возвращает площадь треугольника со стороной a и высотой h, проведённой к этой стороне
    
    Параметры:
        a(double): сторона
        h(double): высота

    Возвращаемое значение:
        S(double): площадь треугольника
    '''
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Возвращает периметр треугольника со сторонами a, b, c

    Параметры:
        a(double): 1-ая сторона треугольника
        b(double): 2-ая сторона треугольника
        c(double): 3-я сторона треугольника
    
    Возвращаемое значение:
        P(double): периметр треугольника
    '''
    return a + b + c 
