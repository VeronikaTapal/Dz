from datetime import datetime

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.validate_date()
        self.print_date()

    def validate_date(self):
        if self.day > self.days_in_month():
            raise ValueError("Некорректное количество дней в месяце")

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def days_in_month(self):
        if self.month in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        elif self.month in {4, 6, 9, 11}:
            return 30
        else:
            return 29 if self.is_leap_year() else 28

    def print_date(self):
        month_names = {
            1: "Январь",
            2: "Февраль",
            3: "Март",
            4: "Апрель",
            5: "Май",
            6: "Июнь",
            7: "Июль",
            8: "Август",
            9: "Сентябрь",
            10: "Октябрь",
            11: "Ноябрь",
            12: "Декабрь"
        }
        month_name = month_names.get(self.month)
        if month_name:
            print(f"{self.day} {month_name} {self.year}")
        else:
            print("Некорректное значение месяца")

class DateStamp(Date):
    def __init__(self):
        now = datetime.now()
        super().__init__(now.day, now.month, now.year)

date_stamp = DateStamp()


