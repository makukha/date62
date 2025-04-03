from datetime import datetime, tzinfo  # noqa: F401 # needed for typing
import sys

try:
    from datetime import timezone
except ImportError:
    timezone = object  # type: ignore[assignment,misc]  # need to assign

try:
    from typing import Optional  # noqa: F401 # needed for typing
except ImportError:
    pass

from .codec import encode_date, encode_datetime


def now(prec=2, shortcut=True, tz=None):  # type: (int, bool, Optional[tzinfo]) -> str
    return encode_datetime(datetime.now(tz=tz), prec=prec, shortcut=shortcut)


def today(shortcut=True):  # type: (bool) -> str
    return encode_date(datetime.today(), shortcut=shortcut)


def utcnow(prec=2, shortcut=True):  # type: (int, bool) -> str
    if sys.version_info < (3, 2):  # pragma: nocover  # coverage runs on Python 3
        t = datetime.utcnow()
    else:
        t = datetime.now(tz=timezone.utc)
    ret = encode_datetime(t, prec=prec, shortcut=shortcut)
    return ret
