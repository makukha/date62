from decimal import Decimal
from datetime import date, datetime, time

try:
    from typing import Optional, Union  # noqa: F401 # needed for typing
except ImportError:
    pass

from .base62 import decode_int, encode_int


def decode(value):  # type: (str) -> Union[date, datetime, time, Decimal]
    if len(value) == 4:
        return decode_date(value)
    elif len(value) == 5:
        return decode_time(value)
    elif len(value) in (7, 9, 11):
        return decode_datetime(value)
    elif len(value) >= 13 and len(value) % 2 == 0:
        return decode_timestamp(value)
    else:
        raise ValueError('Invalid date62 string')


def encode(value, prec=0, shortcut=False):  # type: (Union[date, time, datetime, int, float, Decimal], int, bool) -> str
    if isinstance(value, datetime):
        return encode_datetime(value, prec=prec, shortcut=shortcut)
    elif isinstance(value, date):
        return encode_date(value, shortcut=shortcut)
    elif isinstance(value, time):
        return encode_time(value, prec=prec)
    elif isinstance(value, (int, float, Decimal)):
        return encode_timestamp(value, prec=prec)
    else:
        raise TypeError('Unexpected type {}'.format(type(value)))


# date


def decode_date(text):  # type: (str) -> date
    """
    Parse Date62 string as date.
    """
    if len(text) != 4:
        raise ValueError('Date62 date string must have 4 characters')

    y, m, d = text[0:2], text[2:3], text[3:4]
    if '00' <= y <= '69':
        year = 2000 + int(y)
    elif '70' <= y <= '99':
        year = 1900 + int(y)
    else:
        year = decode_int(y)

    ret = date(year, decode_int(m), decode_int(d))
    return ret


def encode_date(value, shortcut=False):  # type: (date, bool) -> str
    """
    Encode date as Date62 string.
    """
    if shortcut and 1970 <= value.year <= 1999:
        y = str(value.year - 1900)
    elif shortcut and 2000 <= value.year <= 2069:
        y = str(value.year - 2000)
    else:
        y = encode_int(value.year).zfill(2)

    ret = '{y}{m}{d}'.format(y=y, m=encode_int(value.month), d=encode_int(value.day))
    return ret


# datetime


def decode_datetime(text):  # type: (str) -> datetime
    """
    Parse Date62 string as datetime.
    """
    raise NotImplementedError


def encode_datetime(value, prec=0, shortcut=False):  # type: (datetime, int, bool) -> str
    """
    Encode datetime as Date62 string.
    """
    if prec < 0:
        raise ValueError('Precision must be greater than or equal to 0')

    ret = '{date}{time}'.format(
        date=encode_date(value.date(), shortcut=shortcut),
        time=encode_time(value.time(), prec=prec),
    )
    return ret


# time


def decode_time(text):  # type: (str) -> time
    """
    Parse Date62 string as time.
    """
    raise NotImplementedError


def encode_time(value, prec=0):  # type: (time, int) -> str
    """
    Encode time as Date62 string.
    """
    if prec < 0:
        raise ValueError('Precision must be greater than or equal to 0')

    if prec == 0:
        frac = ''
    else:
        frac = encode_fraction(Decimal(value.microsecond) / 10**6, prec=prec)

    ret = '{hours}{minutes}{seconds}{frac}'.format(
        hours=encode_int(value.hour),
        minutes=encode_int(value.minute),
        seconds=encode_int(value.second),
        frac=frac,
    )
    return ret


# timestamp


def decode_timestamp(text):  # type: (str) -> Decimal
    """
    Parse Date62 string as POSIX timestamp.
    """
    raise NotImplementedError


def encode_timestamp(value, prec=0, shortcut=False):  # type: (Union[int, float, Decimal], int, bool) -> str
    """
    Encode POSIX timestamp as Date62 datetime string.
    """
    if prec < 0:
        raise ValueError('Precision must be greater than or equal to 0')

    value = Decimal(value)
    seconds, frac = divmod(value, 1)
    dtm = encode_datetime(datetime.fromtimestamp(int(seconds)), shortcut=shortcut)

    ret = '{}{}'.format(dtm, encode_fraction(frac, prec=prec)) if prec else dtm
    return ret


# fraction


def encode_fraction(value, prec=None):  # type: (Decimal, Optional[int]) -> str
    if value < 0:
        raise ValueError('Value must be non-negative')
    elif value >= 1:
        raise ValueError('Value must be less than 1')

    if prec is None:
        pass  # use precision of input value
    elif prec < 1:
        raise ValueError('Precision must be greater than or equal to 1')

    # chop value in 3-digit chunks
    chunks = [0] if value == 0 else []
    res = value
    while res > 0:
        head, res = divmod(res * 1000, 1)
        chunks.append(int(head))

    # convert int to base62 and merge
    ret = ''.join(encode_int(chunk).zfill(2) for chunk in chunks)
    return ret
