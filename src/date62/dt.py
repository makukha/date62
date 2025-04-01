from datetime import date, datetime
from functools import partial
from typing import Union

from .conv import (
    date_to_date62,
    date62_to_date,
    datetime_to_date62,
    date62_to_datetime,
)


def from_date62(
    text: str,
) -> Union[date, datetime]:
    if len(text) == 4:
        return date62_to_date(text)
    elif len(text) >= 5:
        return date62_to_datetime(text)
    else:
        raise ValueError('Invalid date62 string, at least 4 characters required')


def to_date62(
    dt: Union[date, datetime],
    *,
    precision: int = 0,
    shortcut: bool = False,
) -> str:
    if isinstance(dt, datetime):
        return datetime_to_date62(dt, precision=precision, shortcut=shortcut)
    elif isinstance(dt, date):
        return date_to_date62(dt, shortcut=shortcut)
    else:
        raise TypeError(f'Unsupported date62 input type: {type[dt]}')


to_date62s = partial(to_date62, shortcut=True)
