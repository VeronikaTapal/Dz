class Date:
    def __init__(self):
        self.input_date()
        self.print_date()

    def validate_date(self):
        if self.day > self.days_in_month():
            raise ValueError("Некорректное количество дней в месяце")


    def input_date(self):
        self.year = int(input("Введите год: "))
        self.month = int(input("Введите месяц (число): "))
        self.day = int(input("Введите день: "))
        if self.day > self.days_in_month():
            raise ValueError("Некорректное количество дней в месяце")

    def is_leap_year(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0:
            return True
        else:
            return False

    def days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month == 2:
            if self.is_leap_year():
                return 29
            else:
                return 28
        else:
            return 30

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

Date()
