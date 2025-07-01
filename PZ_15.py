import sqlite3
from datetime import date

def create_database():
    conn = sqlite3.connect('dry_cleaning.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Услуги (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        мастер_ФИО TEXT NOT NULL,
        клиент_ФИО TEXT NOT NULL,
        тип_чистки TEXT NOT NULL,
        стоимость REAL NOT NULL,
        скидка REAL DEFAULT 0,
        дата_заказа DATE DEFAULT CURRENT_DATE
    )
    ''')
    
    conn.commit()
    conn.close()

create_database()