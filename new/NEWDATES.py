class Date:
    def __init__(self, year, month, day):
        self.day = day
        self.month = month
        self.year = year
        self.validate()

    def validate(self):
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

    def __str__(self):
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
            return f"{self.day} {month_name} {self.year}"
        else:
            return "Некорректное значение месяца"


class DateStamp(Date):
    def __add__(self, other):
        new_day = self.day + other.day
        new_month = self.month + other.month
        new_year = self.year + other.year

        if new_day > 30:
            new_day -= 30
            new_month += 1

        if new_month > 12:
            new_month -= 12
            new_year += 1

        if new_day < 1:
            new_day += 30
            new_month -= 1

        if new_month < 1:
            new_month += 12
            new_year -= 1

        return DateStamp(new_year, new_month, new_day)

    def __sub__(self, other):
        new_day = self.day - other.day
        new_month = self.month - other.month
        new_year = self.year - other.year

        if new_day < 1:
            new_month -= 1
            if new_month < 1:
                new_month += 12
                new_year -= 1

            days_in_month = self.days_in_month(new_month, new_year)
            new_day += days_in_month

        if new_month < 1:
            new_month += 12
            new_year -= 1

        return DateStamp(new_year, new_month, new_day)
