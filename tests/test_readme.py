from dateutil.parser import parse
import pytest
import re
from typing import assert_never

from date62 import to_date62, to_date62s


RX_REMOVE = re.compile(r'[^0-9]+')


@pytest.mark.parametrize(
    'typ,text,d62,d62s,args',
    [
        ('date', '2024-Dec-29', 'WeCT', '24CT', {}),
        ('date', '2025-Jan-01', 'Wf11', '2511', {}),
        ('datetime', '2025-Jan-01 T00:01:02', 'Wf11012', '2511012', {}),
        ('datetime', '2025-Jan-01 00:01:02.345', 'Wf110125Z', '25110125Z', dict(precision=1)),
        ('datetime', '2025-Jan-01 00:01:02.345678', 'Wf110125ZAw', '25110125ZAw', dict(precision=2)),
        ('datetime', '2025-Jan-01 00:01:02.345678012', 'Wf110125ZAw0C', '25110125ZAw0C', dict(precision=3, subsec=345678012)),
    ],
)
def test_readme(typ: str, text: str, d62: str, d62s: str, args: dict):
    if typ == 'date':
        dt = parse(text).date()
    elif typ == 'datetime':
        dt = parse(text)
    else:
        assert_never(typ)

    assert to_date62(dt, **args) == d62
    assert to_date62s(dt, **args) == d62s
