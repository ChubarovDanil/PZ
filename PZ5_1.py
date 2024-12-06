#Составить функцию, которая напечатает сорок любых символов. 
import random
import string
#Импортируем модуль random для генерации случайных символов и модуль string, который содержит наборы символов.

def print_random_characters(count=40):
    # Генерируем случайные символы из букв, цифр и специальных символов
    characters = random.choices(string.ascii_letters + string.digits + string.punctuation, k=count)
#Используем random.choices() для выбора случайных символов из объединения строчных и заглавных букв, цифр и специальных символов. 
#Параметр k=count указывает, сколько символов нужно сгенерировать.
    print(''.join(characters))
#Соединяем список символов в строку с помощью ''.join() и выводим её на экран.
# Вызов функции
print_random_characters()