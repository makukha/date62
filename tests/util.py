from datetime import date, datetime
from unittest import TestCase  # noqa: F401 # needed for typing

try:
    from collections.abc import Callable  # noqa: F401 # needed for typing
    from typing import Any, Union  # noqa: F401 # needed for typing
except ImportError:
    pass


def assertFunction(self, f, x, y):  # type: (TestCase, Callable[[Any], Any], object, Any) -> None
    if is_exception(y):
        with self.assertRaises(y):
            f(x)
    else:
        self.assertEqual(y, f(x))


def dt(text):  # type: (str) -> Union[date, datetime, None]
    for typ, fmt in (
        (date, '%Y-%b-%d'),
        (datetime, '%Y-%b-%d %H:%M:%S'),
        (datetime, '%Y-%b-%d %H:%M:%S.%f'),
    ):
        try:
            value = datetime.strptime(text, fmt)
            return value.date() if typ is date else value
        except ValueError:
            continue
    return None


def is_exception(x):  # type: (object) -> bool
    return isinstance(x, type) and issubclass(x, Exception)
