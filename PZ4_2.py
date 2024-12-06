#Найти количество квадратов, размещенных на прямоугольнике. Операции
#умножения и деления не использовать.
def count_squares(A, B, C):
#Подсчитывает количество квадратов со стороной C, которые можно разместить на прямоугольнике A x B.
    
    # Подсчет квадратов по ширине
    count_width = 0
    remaining_width = A
    
    while remaining_width >= C:
        count_width += 1
        remaining_width -= C

    # Подсчет квадратов по высоте
    count_height = 0
    remaining_height = B
    
    while remaining_height >= C:
        count_height += 1
        remaining_height -= C

    # Общее количество квадратов
    total_squares = 0
    for _ in range(count_height):
        total_squares += count_width

    return total_squares

# Пример использования
A = int(input("Введите длину прямоугольника A: "))
B = int(input("Введите ширину прямоугольника B: "))
C = int(input("Введите сторону квадрата C: "))

if A > 0 and B > 0 and C > 0:
    result = count_squares(A, B, C)
    print(f"Количество квадратов со стороной {C}, размещенных на прямоугольнике {A} x {B}: {result}")
else:
    print("Пожалуйста, введите положительные числа для A, B и C.")