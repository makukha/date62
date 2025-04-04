from datetime import datetime, tzinfo  # noqa: F401 # needed for typing

try:
    from datetime import timezone
except ImportError:
    timezone = object  # type: ignore[assignment,misc]  # need to assign

try:
    from typing import Optional  # noqa: F401 # needed for typing
except ImportError:
    pass

from .codec import encode_date, encode_datetime


_datetime_now = datetime.now
_datetime_today = datetime.today


def now(prec=2, scut=True, tz=None):  # type: (int, bool, Optional[tzinfo]) -> str
    return encode_datetime(_datetime_now(tz=tz), prec=prec, scut=scut)


def today(scut=True):  # type: (bool) -> str
    return encode_date(_datetime_today(), scut=scut)
