CHARS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def decode_int(text):  # type: (str) -> int
    try:
        return sum(62**i * CHARS.index(c) for i, c in enumerate(reversed(text)))
    except ValueError:
        raise ValueError('Non-alphanumeric character in Date62 string')  # noqa: B904 # raise ... from not supported by legacy Python


def encode_int(value):  # type: (int) -> str
    if value < 0:
        raise ValueError('Negative integers are not supported')
    digits = []  # type: list[str]
    while True:
        value, d = divmod(value, 62)
        digits.insert(0, CHARS[d])
        if value == 0:
            break
    return ''.join(digits)
