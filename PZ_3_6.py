def is_point_inside_rectangle(x, y, x1, y1, x2, y2):
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 < y2:
        y1, y2 = y2, y1
    
    return x1 <= x <= x2 and y2 <= y <= y1

x, y = 3, 4
x1, y1 = 2, 5
x2, y2 = 4, 3

if is_point_inside_rectangle(x, y, x1, y1, x2, y2):
    print("Точка лежит внутри прямоугольника.")
else:
    print("Точка не лежит внутри прямоугольника.")