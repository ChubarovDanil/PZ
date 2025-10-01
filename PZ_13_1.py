#В двумерном списке элементы последнего столбца заменить на -1.
def replace_last_column(matrix):
    for row in matrix:
        if row: 
            row[-1] = -1
    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

result = replace_last_column(matrix)

print("\nМатрица после замены последнего столбца:")
for row in result:

    print(row)
