import random

N = 10 
original_sequence = [random.randint(-100, 100) for _ in range(N)]

positive_even = [x for x in original_sequence if x > 0 and x % 2 == 0]

sum_pe = sum(positive_even)
average_pe = sum_pe / len(positive_even) if positive_even else 0

print("Исходная последовательность:", original_sequence)
print("Положительные четные элементы:", positive_even)
print("Количество положительных четных элементов:", len(positive_even))
print("Сумма положительных четных элементов:", sum_pe)
print("Среднее арифметическое положительных четных элементов:", average_pe)