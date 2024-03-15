import pytest
from freezegun import freeze_time
from NEWDATES import DateStamp
from NEWDATES import Date

@freeze_time("2024-03-10")
def test_datestamp_init():
    datestamp = DateStamp(2024, 3, 10)
    assert datestamp.year == 2024
    assert datestamp.month == 3
    assert datestamp.day == 10

def test_datestamp_add():
    date1 = DateStamp(2024, 2, 29)
    date2 = DateStamp(2024, 3, 31)
    new_date = date1 + date2
    assert str(new_date) == "30 Июнь 4048"


def test_datestamp_subtract():
    date1 = DateStamp(2022, 1, 15)
    date2 = DateStamp(2020, 11, 5)
    new_date = date1 - date2
    assert str(new_date) == "10 Февраль 1"

def test_date_datestamp_subtract():
    date1 = DateStamp(2022, 1, 15)
    date2 = Date(2020, 11, 5)
    new_date = date1 - date2
    assert str(new_date) == "10 Февраль 1"


def test_Date_invalid_date():
    with pytest.raises(ValueError):
        Date(32, 13, 2022)  # Передаем неверную дату

def test_Date_specific_date():
    specific_date = Date(2000, 1, 1)  # Дата, которую можно добавить в код
    assert specific_date.day == 1
    assert specific_date.month == 1
    assert specific_date.year == 2000
