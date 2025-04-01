from typing import Union

import pytest

from date62.conv import int_to_base62, base62_to_int


@pytest.mark.parametrize(
    'num,base62',
    (
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
)
def test_int_to_str(num: int, base62: Union[str, type[Exception]]):
    if isinstance(base62, str):
        assert int_to_base62(num) == base62
        assert base62_to_int(base62) == num
    elif isinstance(base62, type) and issubclass(base62, Exception):
        with pytest.raises(base62):
            int_to_base62(num)
    else:
        raise AssertionError('unreachable')


# fmt: off
@pytest.mark.parametrize(
    'base62,num',
    (
        ('00', 0),
    ),
)
# fmt: on
def test_str_to_int(base62: str, num: Union[int, type[Exception]]):
    if isinstance(num, int):
        assert base62_to_int(base62) == num
    elif isinstance(num, type) and issubclass(num, Exception):
        with pytest.raises(num):
            base62_to_int(base62)
    else:
        raise AssertionError('unreachable')
