import datetime

class Calendar:
    def __init__(self, year, month, day):
        """
        Инициализация календаря с указанными годом, месяцем и днем
        :param year: год (целое число)
        :param month: месяц (целое число от 1 до 12)
        :param day: день (целое число от 1 до 31)
        """
        self.year = year
        self.month = month
        self.day = day
        
        # Проверка корректности даты
        try:
            self.date = datetime.date(year, month, day)
        except ValueError as e:
            raise ValueError("Некорректная дата") from e
    
    def get_weekday(self):
        """
        Возвращает день недели для указанной даты
        :return: строка с названием дня недели
        """
        weekdays = ["Понедельник", "Вторник", "Среда", 
                   "Четверг", "Пятница", "Суббота", "Воскресенье"]
        return weekdays[self.date.weekday()]
    
    def is_leap_year(self):
        """
        Проверяет, является ли год високосным
        :return: True если год високосный, иначе False
        """
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
    
    def days_in_month(self):
        """
        Возвращает количество дней в месяце
        :return: целое число дней
        """
        if self.month == 2:
            return 29 if self.is_leap_year() else 28
        elif self.month in [4, 6, 9, 11]:
            return 30
        else:
            return 31
    
    def __str__(self):
        return f"Дата: {self.day:02d}.{self.month:02d}.{self.year}"


# Пример использования
if __name__ == "__main__":
    try:
        # Создаем объект календаря
        cal = Calendar(2023, 11, 15)
        
        print(cal)
        print(f"День недели: {cal.get_weekday()}")
        print(f"Високосный год: {'Да' if cal.is_leap_year() else 'Нет'}")
        print(f"Дней в месяце: {cal.days_in_month()}")
        
        print("\nПроверка для високосного года:")
        cal_leap = Calendar(2024, 2, 1)
        print(cal_leap)
        print(f"Високосный год: {'Да' if cal_leap.is_leap_year() else 'Нет'}")
        print(f"Дней в месяце: {cal_leap.days_in_month()}")
        
    except ValueError as e:
        print(f"Ошибка: {e}")