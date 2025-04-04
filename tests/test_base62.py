from unittest import TestCase

from date62 import base62
from tests.util import assertFunction, is_exception


class TestBase62(TestCase):
    def test_decode_int(
        self,
        cases=(
            # edge cases
            ('00', 0),
        ),
    ):  # type: (tuple[tuple[object, object], ...]) -> None
        for case in cases:
            x, y = case
            assertFunction(self, base62.decode_int, x, y)

    def test_encode_int(
        self,
        cases=(
            # valid input
            (0, '0'),
            (10, 'A'),
            (61, 'z'),
            (62**3, '1000'),
            (62**3 - 1, 'zzz'),
            (2024, 'We'),
            (2025, 'Wf'),
            (1970, 'Vm'),
            (2069, 'XN'),
            (128, '24'),  # 62 * 2 + 4
            (381, '69'),  # 62 * 6 + 9
            (434, '70'),  # 62 * 7 + 0
            (567, '99'),  # 62 * 9 + 9
            (3843, 'zz'),  # 62 * 61 + 61
            (999, 'G7'),
            (999999, '4C91'),
            (999999999, '15ftgF'),
            (999999999999, 'HbXm5a3'),
            (12, 'C'),
            (29, 'T'),
            (30, 'U'),
            (31, 'V'),
            (345, '5Z'),
            (678, 'Aw'),
            # invalid input
            (-1, ValueError),
            ('', TypeError),
        ),
    ):  # type: (tuple[tuple[object, object], ...]) -> None
        for case in cases:
            x, y = case
            assertFunction(self, base62.encode_int, x, y)
            if not is_exception(y):  # asser reverse for better coverage
                assertFunction(self, base62.decode_int, y, x)
