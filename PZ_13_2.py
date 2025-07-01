def replace_third_row(matrix, new_row):
    
    if len(matrix) >= 3:
        
        if len(new_row) == len(matrix[2]):
            matrix[2] = new_row.copy() 
        else:
            print("Ошибка: несоответствие размерностей")
    else:
        print("Ошибка: в матрице меньше 3 строк")
    return matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

new_row = [20, 21, 22]

print("Исходная матрица:")
for row in matrix:
    print(row)


result = replace_third_row(matrix, new_row)

print("\nМатрица после замены третьей строки:")
for row in result:
    print(row)