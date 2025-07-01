def lowercase_generator(input_sequence):
    """Генератор, преобразующий все буквенные символы в строчные"""
    for item in input_sequence:
        if isinstance(item, str):
            yield item.lower()
        else:
            yield item

input_data = ['Hello', 'WORLD', 42, 'PyThOn', '123', 'СъЕШЬ ещё этих МяГкИх Французских Булок']
result = list(lowercase_generator(input_data))

print("Исходные данные:", input_data)
print("После преобразования:", result)