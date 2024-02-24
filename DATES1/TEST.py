from DATES import Date
import pytest

def test_days_in_month():
    date = Date(2022, 2, 1)
    assert date.days_in_month() == 28

    date = Date(2020, 2, 1)
    assert date.days_in_month() == 29

    date = Date(2022, 4, 1)
    assert date.days_in_month() == 30

def test_is_leap_year():
    date = Date(2022, 1, 1)
    assert not date.is_leap_year()

    date = Date(2020, 1, 1)
    assert date.is_leap_year()

def test_print_date():
    date = Date(2022, 12, 31)
    assert date.print_date() == "31 Декабря 2022"



