from copy import copy
from datetime import date, datetime, timedelta
import re


# date


def date62_to_date(text: str) -> date:
    """
    Parse string as Date62.
    """
    if len(text) != 4:
        raise ValueError('Date62 date string must have 4 characters')
    yy, m, d = text[0:2], text[2:3], text[3:4]
    if '00' <= yy <= '69':
        year = 2000 + int(yy)
    elif '70' <= yy <= '99':
        year = 1900 + int(yy)
    else:
        year = base62_to_int(yy)
    return date(year, base62_to_int(m), base62_to_int(d))


def date_to_date62(dt: date, *, shortcut: bool = False) -> str:
    """
    Convert date to Date62 string.
    """
    if shortcut and 1970 <= dt.year <= 1999:
        yy = str(dt.year - 1900)
    elif shortcut and 2000 <= dt.year <= 2069:
        yy = str(dt.year - 2000)
    else:
        yy = int_to_base62(dt.year).zfill(2)
    return f'{yy}{int_to_base62(dt.month)}{int_to_base62(dt.day)}'


# datetime


def date62_to_datetime(value: str) -> datetime:
    raise NotImplementedError


def datetime_to_date62(
    dt: datetime,
    *,
    precision: int = 0,
    shortcut: bool = False,
) -> str:
    """
    Convert datetime to Date62 string.
    """
    if precision < 0:
        raise ValueError('Precision must be greater than or equal to 0')

    # get sub-seconds from microseconds
    if 0 <= precision <= 1:
        subsec = int(round(dt.microsecond / 1000 ** (2 - precision)))
        if subsec == 1000:
            dt = copy(dt)
            dt += timedelta(seconds=1)
            subsec = 0
    elif precision == 2:
        subsec = dt.microsecond
    else:
        subsec = dt.microsecond * 1000 ** (precision - 2)

    subdig: list[str] = []
    for _ in range(precision):
        subsec, rest = divmod(subsec, 1000)
        subdig.insert(0, int_to_base62(rest).zfill(2))

    return (
        f'{date_to_date62(dt.date(), shortcut=shortcut)}'
        f'{int_to_base62(dt.hour)}'
        f'{int_to_base62(dt.minute)}'
        f'{int_to_base62(dt.second)}'
        f'{"".join(subdig)}'
    )


# int


BASE62_ALPHA = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
RX_BASE62_ALPHA = re.compile(rf'[{BASE62_ALPHA}]*')


def base62_to_int(text: str) -> int:
    try:
        return sum(62**i * BASE62_ALPHA.index(c) for i, c in enumerate(reversed(text)))
    except ValueError as exc:
        raise ValueError('Non-alphanumeric character in Date62 string') from exc


def int_to_base62(num: int) -> str:
    if not isinstance(num, int):
        raise TypeError('Expected integer')
    if num < 0:
        raise ValueError('Negative numbers are not supported')
    digits: list[str] = []
    while True:
        num, d = divmod(num, 62)
        digits.insert(0, BASE62_ALPHA[d])
        if num == 0:
            break
    return ''.join(digits)
