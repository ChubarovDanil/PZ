a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = a + b
if c % 5 == 0:
    result = c + 5
else:
    result = c - 1
print(result)