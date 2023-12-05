year = int(input())


def is_year_leap(year):
    print("Год", year, ":", "Високосный" if year % 4 == 0 else "Нет")

is_year_leap(year)