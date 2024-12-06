#Преобразовать список, увеличив каждый его элемент на исходное значение элемента
def transform_list(A, K):
    # Получаем значение элемента Ak (с учетом нулевой индексации)
    value_to_add = A[K - 1]
    # Преобразуем список, увеличивая каждый элемент на значение Ak с помощью map
    transformed_list = list(map(lambda x: x + value_to_add, A))
    return transformed_list

A = [1, 2, 3, 4, 5]
K = 3
result = transform_list(A, K)
print(result)