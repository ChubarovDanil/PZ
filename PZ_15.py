#Приложение ХИМЧИСТКА для некоторой организации. БД должна содержать 
#таблицу Услуги со следующей структурой записи: ФИО мастера, ФИО клиента, тип 
#чистки, стоимость, скидка. 
import sqlite3

def create_connection():
    """Создает подключение к базе данных SQLite."""
    conn = sqlite3.connect('himchistka.db')
    return conn

def create_table(conn):
    """Создает таблицу 'Uslugi', если она еще не существует."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Uslugi (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                master_name TEXT NOT NULL,
                client_name TEXT NOT NULL,
                cleaning_type TEXT NOT NULL,
                cost REAL NOT NULL,
                discount REAL NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при создании таблицы: {e}")

def insert_initial_data(conn):
    """Заполняет таблицу минимум 2 записями."""
    data = [
        ("Иванов Иван", "Петров Петр", "Классическая", 1500, 10),
        ("Сидорова Мария", "Смирнов Алексей", "Химчистка", 2000, 5)
    ]
    try:
        cursor = conn.cursor()
        cursor.executemany('''
            INSERT INTO Uslugi (master_name, client_name, cleaning_type, cost, discount)
            VALUES (?, ?, ?, ?, ?)
        ''', data)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении данных: {e}")

def add_record(conn):
    """Добавляет новую запись в таблицу."""
    try:
        master_name = input("Введите ФИО мастера: ")
        client_name = input("Введите ФИО клиента: ")
        cleaning_type = input("Введите тип чистки: ")
        cost = float(input("Введите стоимость: "))
        discount = float(input("Введите скидку: "))
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Uslugi (master_name, client_name, cleaning_type, cost, discount)
            VALUES (?, ?, ?, ?, ?)
        ''', (master_name, client_name, cleaning_type, cost, discount))
        conn.commit()
        print("Запись успешно добавлена.")
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении: {e}")
    except ValueError:
        print("Некорректный ввод числовых значений.")

def search_records(conn):
    """Поиск записей по разным критериям, используя 3 варианта SQL-запросов."""
    print("Выберите критерий поиска:")
    print("1 - по ФИО мастера")
    print("2 - по ФИО клиента")
    print("3 - по типу чистки")
    choice = input("Введите номер варианта: ")

    cursor = conn.cursor()
    if choice == '1':
        name = input("Введите ФИО мастера: ")
        # Вариант 1: точное совпадение
        cursor.execute("SELECT * FROM Uslugi WHERE master_name = ?", (name,))
    elif choice == '2':
        name = input("Введите ФИО клиента: ")
        # Вариант 2: поиск по части строки (LIKE)
        cursor.execute("SELECT * FROM Uslugi WHERE client_name LIKE ?", ('%' + name + '%',))
    elif choice == '3':
        c_type = input("Введите тип чистки: ")
        # Вариант 3: по цене, например, стоимость больше определенного
        cursor.execute("SELECT * FROM Uslugi WHERE cleaning_type = ?", (c_type,))
    else:
        print("Некорректный выбор.")
        return

    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("Записи не найдены.")

def delete_record(conn):
    """Удаляет записи по условиям, используя 3 варианта SQL-запросов."""
    print("Выберите критерий удаления:")
    print("1 - по ФИО мастера")
    print("2 - по ФИО клиента")
    print("3 - по типу чистки")
    choice = input("Введите номер варианта: ")

    cursor = conn.cursor()
    if choice == '1':
        name = input("Введите ФИО мастера: ")
        # Вариант 1: = оператор
        cursor.execute("DELETE FROM Uslugi WHERE master_name = ?", (name,))
    elif choice == '2':
        name = input("Введите ФИО клиента: ")
        # Вариант 2: LIKE оператор
        cursor.execute("DELETE FROM Uslugi WHERE client_name LIKE ?", ('%' + name + '%',))
    elif choice == '3':
        c_type = input("Введите тип чистки: ")
        # Вариант 3: удаление по типу
        cursor.execute("DELETE FROM Uslugi WHERE cleaning_type = ?", (c_type,))
    else:
        print("Некорректный выбор.")
        return
    conn.commit()
    print(f"Удалено записей: {cursor.rowcount}")

def edit_record(conn):
    """Редактирует запись по ID, позволяя изменить выбранное поле."""
    try:
        record_id = int(input("Введите ID записи для редактирования: "))
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Uslugi WHERE id = ?", (record_id,))
        record = cursor.fetchone()
        if not record:
            print("Запись с таким ID не найдена.")
            return
        print("Выберите поле для редактирования:")
        print("1 - ФИО мастера")
        print("2 - ФИО клиента")
        print("3 - Тип чистки")
        print("4 - Стоимость")
        print("5 - Скидка")
        field_choice = input("Введите номер поля: ")

        if field_choice == '1':
            new_value = input("Введите новое ФИО мастера: ")
            field = 'master_name'
        elif field_choice == '2':
            new_value = input("Введите новое ФИО клиента: ")
            field = 'client_name'
        elif field_choice == '3':
            new_value = input("Введите новый тип чистки: ")
            field = 'cleaning_type'
        elif field_choice == '4':
            new_value = float(input("Введите новую стоимость: "))
            field = 'cost'
        elif field_choice == '5':
            new_value = float(input("Введите новую скидку: "))
            field = 'discount'
        else:
            print("Некорректный выбор.")
            return
        # Обновление выбранного поля
        cursor.execute(f"UPDATE Uslugi SET {field} = ? WHERE id = ?", (new_value, record_id))
        conn.commit()
        print("Запись успешно обновлена.")
    except sqlite3.Error as e:
        print(f"Ошибка при редактировании: {e}")
    except ValueError:
        print("Некорректный ввод числовых значений.")

def main():
    """Основная функция программы."""
    conn = create_connection()
    create_table(conn)
    # Проверка наличия данных, и добавление минимум 2
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Uslugi")
    count = cursor.fetchone()[0]
    if count < 2:
        insert_initial_data(conn)

    while True:
        print("\nМеню:")
        print("1 - Добавить услугу")
        print("2 - Поиск услуги")
        print("3 - Удалить услугу")
        print("4 - Редактировать услугу")
        print("5 - Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            add_record(conn)
        elif choice == '2':
            search_records(conn)
        elif choice == '3':
            delete_record(conn)
        elif choice == '4':
            edit_record(conn)
        elif choice == '5':
            print("Завершение работы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

    conn.close()

if __name__ == "__main__":
    main()

