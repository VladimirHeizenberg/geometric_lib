[![example workflow](https://github.com/VladimirHeizenberg/geometric_lib/actions/workflows/linting.yml/badge.svg)](https://github.com/VladimirHeizenberg/geometric_lib/actions)
[![example workflow](https://github.com/VladimirHeizenberg/geometric_lib/actions/workflows/test.yml/badge.svg)](https://github.com/VladimirHeizenberg/geometric_lib/actions)
# Общая информация
- Библиотека, позволяющая проводить геометрические расчёты.
- Содержит файлы для расчётов:
  * круга
  * прямоугольника
  * квадрата
  * треугольника

  В каждом файле есть две функции: для вычисления периметра и для вычисления площади соответсвующей фигуры.

# Функции

## Круг (circle.py)

1. **area\(r\)**
Возвращает площадь круга радиусом r
**Параметры:** 
    * r (double): радиус круга

    **Возвращаемое значение:**
    * S (double): площадь круга радиусом r

    **Пример использования**
    ```python
    area(1) # 3.1415926535
    ```

2. **perimeter\(r\)**
Возвращает периметр круга радиусом r
**Параметры:**
    * r(double): радиус круга

    **Возвращаемое значение:**
    * P (double): длина окружности радиуса r
    
    **Пример использования**
    ```python
    perimeter(1) # 6.2831853
    ```
    
## Прямоугольник (rectangle.py)

1. **area(a, b)**
Возвращает площадь прямоугольника со сторонами a и b
**Параметры:** 
    * a (double): 1-ая сторона прямоугольника
    * b (double): 2-ая сторона прямоугольника

    **Возвращаемое значение:**
    * S (double): площадь прямоугольника со сторонами a и b
    
    **Пример использования**
    ```python
    area(3, 4) # 12
    ```

2. **perimeter(a, b)**
Возвращает периметр прямоугольника со сторонами a и b
**Параметры:** 
    * a (double): 1-ая сторона прямоугольника
    * b (double): 2-ая сторона прямоугольника

    **Возвращаемое значение:**
    * P (double): периметр прямоугольника со сторонами a и b
    
    **Пример использования**
    ```python
    perimeter(3, 4) # 14
    ```
    
## Квадрат (square.py)

1. **area(a)**
Возвращает площадь квадрата со стороной a.
**Параметры:**
    * a (double): сторона квадрата

    **Возвращаемое значение:**
    * S (double): площадь квадратат со стороной a.
    
    **Пример использования**
    ```python
    area(3) # 9
    ```

2. **perimeter(a)**
Возвращает периметр квадрата со стороной a.
**Параметры:**
    * a (double): сторона квадрата

    **Возвращаемое значение:**
    * P (double): периметр квадрата со стороной a.
    
    **Пример использования**
    ```python
    perimeter(3) # 12
    ```
    
## Треугольник (triangle.py)

1. **area(a, h)**
Возвращает площадь треугольника со стороной a и высотой h, проведённой к этой стороне
**Параметры:**
    * a (double): сторона
    * h (double): высота

    **Возвращаемое значение:**
    * S (double): площадь треугольника
    
    **Пример использования**
    ```python
    area(3, 4) # 6
    ```
    
2. **perimeter\(r\)**
Возвращает периметр треугольника со сторонами a, b, c
**Параметры:**
    * a (double): 1-ая сторона треугольника
    * b (double): 2-ая сторона треугольника
    * c (double): 3-я сторона треугольника
    
    **Возвращаемое значение:**
        P (double): периметр треугольника

    **Пример использования**
    ```python
    perimeter(3, 4, 5) # 12
    ```

# Список коммитов

## 1d76f55
- **Author:** Vladimir
- **Date:** 2024-21-11
- **Message:** add tests

## c9ee6d8
- **Author:** Vladimir
- **Date:** 2024-10-09
- **Message:** docs in code files

## f76ab65
- **Author:** Vladimir
- **Date:** 2024-10-09
- **Message:** Initial commit

## bf10355
- **Author:** Vladimir
- **Date:** 2024-09-25
- **Message:** add file triangle.py and correct rectangle.py

## 19e9b6a
- **Author:** Vladimir
- **Date:** 2024-09-25
- **Message:** add file rectangle.py

## d078c8d
- **Author:** smartiqa
- **Date:** 2021-03-04
- **Message:** L-03: Docs added