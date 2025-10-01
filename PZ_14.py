#В исходном текстовом файле(hotline1.txt) найти всеномера телефонов, 
#соответствующих шаблону 8(000)000-00-00. Посчитать количество полученных 
#элементов. После фразы «Горячая линия» добавить фразу «Министерства 
#образования Ростовской области», выполнив манипуляции в новом файле. 
import re

with open('hotline1.txt', 'r', encoding='utf-8') as file:
    content = file.read()

phone_pattern = r'8\(\d{3}\)\d{3}-\d{2}-\d{2}'
phones = re.findall(phone_pattern, content)
phone_count = len(phones)

print(f"Найдено номеров телефонов: {phone_count}")
for phone in phones:
    print(phone)

new_content = content.replace(
    'Горячая линия',
    'Горячая линия Министерства образования Ростовской области'
)

with open('hotline_new.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(new_content)


print("\nФайл успешно обработан и сохранён как 'hotline_new.txt'")
