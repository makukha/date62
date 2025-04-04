from decimal import Decimal
from unittest import TestCase

try:
    from datetime import date, datetime  # noqa: F401 # needed for typing
    from typing import Optional, Union  # noqa: F401 # needed for typing
except ImportError:
    pass

import date62
from tests.util import dt


def ddt(text):  # type: (str) -> Optional[Decimal]
    dtm, frac = text.split('.')
    d = dt(dtm)
    if d is None:
        ret = None
    elif isinstance(d, datetime):
        timestamp = (d - datetime(1970, 1, 1)).total_seconds()
        ret = Decimal(timestamp) + Decimal('0.{}'.format(frac))
    else:
        raise ValueError('Datetime string required')
    return ret


class TestReadme(TestCase):
    def test_simple(
        self,
        cases=(
            (dt('2024-Dec-29'), 'WeCT', '24CT', 0),
            (dt('2025-Jan-01'), 'Wf11', '2511', 0),
            (dt('2025-Jan-01 00:01:02'), 'Wf11012', '2511012', 0),
            (dt('2025-Jan-01 00:01:02.345'), 'Wf110125Z', '25110125Z', 1),
            (dt('2025-Jan-01 00:01:02.345678'), 'Wf110125ZAw', '25110125ZAw', 2),
        ),
    ):  # type: (tuple[tuple[Union[date, datetime, None], str, str, int], ...]) -> None
        for case in cases:
            value, d62, d62s, prec = case
            assert value is not None  # for typing only
            self.assertEqual(d62, date62.encode(value, prec))
            self.assertEqual(d62s, date62.encode(value, prec, scut=True))

    # fmt: off
    def test_precise(
        self,
        cases=(
            (ddt('2025-Jan-01 00:01:02.345678012'), 'Wf110125ZAw0C', '25110125ZAw0C', 3),
            (ddt('2025-Jan-01 00:01:02.345678012345'), 'Wf110125ZAw0C5Z', '25110125ZAw0C5Z', 4),
        ),
    ):  # type: (tuple[tuple[Optional[Decimal], str, str, int], ...]) -> None
        for case in cases:
            value, d62, d62s, prec = case
            assert value is not None  # for typing only
            self.assertEqual(d62, date62.encode_timestamp(value, prec))
            self.assertEqual(d62s, date62.encode_timestamp(value, prec, scut=True))
    # fmt: off
