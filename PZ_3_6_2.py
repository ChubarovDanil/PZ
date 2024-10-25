A = float(input("Введите координату точки A: "))
B = float(input("Введите координату точки B: "))
C = float(input("Введите координату точки C: "))

distance_B = abs(A - B)
distance_C = abs(A - C)

if distance_B < distance_C:
    closest_point = 'B'
    closest_distance = distance_B
else:
    closest_point = 'C'
    closest_distance = distance_C

print(f"Точка {closest_point} расположена ближе к A с расстоянием {closest_distance:.2f}.")