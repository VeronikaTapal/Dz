from datetime import datetime
import pytest

from NEWDATES import DateStamp

def test_date_stamp_current_date():
    date_stamp = DateStamp()
    now = datetime.now()
    assert date_stamp.day == now.day
    assert date_stamp.month == now.month
    assert date_stamp.year == now.year




