# date62
<!-- docsub: begin -->
<!-- docsub: exec yq '"> " + .project.description' pyproject.toml -->
> Compact string-based date(time) format for logging, data engineering, and visualizations.
<!-- docsub: end -->

<!-- docsub: begin -->
<!-- docsub: include docs/badges.md -->
[![license](https://img.shields.io/github/license/makukha/date62.svg)](https://github.com/makukha/date62/blob/main/LICENSE)
[![pypi](https://img.shields.io/pypi/v/date62.svg#v0.1.0)](https://pypi.org/project/date62)
[![python versions](https://img.shields.io/pypi/pyversions/date62.svg)](https://pypi.org/project/date62)
[![tests](https://raw.githubusercontent.com/makukha/date62/v0.1.0/docs/img/badge/tests.svg)](https://github.com/makukha/date62)
[![coverage](https://raw.githubusercontent.com/makukha/date62/v0.1.0/docs/img/badge/coverage.svg)](https://github.com/makukha/date62)
[![tested with multipython](https://img.shields.io/badge/tested_with-multipython-x)](https://github.com/makukha/multipython)
[![uses docsub](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/makukha/docsub/refs/heads/main/docs/badge/v1.json)](https://github.com/makukha/docsub)
[![mypy](https://img.shields.io/badge/type_checked-mypy-%231674b1)](http://mypy.readthedocs.io)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/ruff)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/10374/badge)](https://www.bestpractices.dev/projects/10374)
<!-- docsub: end -->


# Features

<!-- docsub: begin -->
<!-- docsub: include docs/features.md -->
- Compact: 4 ASCII characters for date, 7 characters for datetime
- URL safe: uses Base62 encoding
- Natural sorting
- Semi-human-readable
- Covers range from 567-Jan-01 to 3843-Dec-31
- Arbitrary sub-second precision
- More readable shortcut form for values between 1970-Jan-01 and 2069-Dec-31
- Timezone info not supported at the moment
- Use cases:
  - Logging timestamps
  - Visualize dates on charts
  - Datetime-based file identifiers
  - Sub-second-precision string labels
<!-- docsub: end -->


# Installation

```shell
$ pip install date62
```


# Examples

<!-- docsub: begin -->
<!-- docsub: include docs/examples.md -->
| date or datetime                  | Date62                     |
|-----------------------------------|----------------------------|
| 2024-Dec-29                       | `24CT`, `WeCT`             |
| 2025-Jan-01                       | `2511`, `Wf11`             |
| 2025-Jan-01 00:01:02              | `2511012`, `Wf11012`       |
| 2025-Jan-01 00:01:02.345          | `25110125Z`, `Wf...`       |
| 2025-Jan-01 00:01:02.345678       | `25110125ZAw`, `Wf...`     |
| 2025-Jan-01 00:01:02.345678012    | `25110125ZAw0C`, `Wf...`   |
| 2025-Jan-01 00:01:02.345678012345 | `25110125ZAw0C5Z`, `Wf...` |
<!-- docsub: end -->


# Usage

<!-- docsub: begin #usage.md -->
<!-- docsub: include docs/usage.md -->
<!-- docsub: begin -->
<!-- docsub: x toc tests/test_usage.py 'Usage.*' -->
* [Encode](#encode)
<!-- docsub: end -->


<!-- docsub: begin -->
<!-- docsub: x cases tests/test_usage.py 'Usage.*' -->
## Encode

Works for `datetime`, `date`, `time`, `int`, `float`, `Decimal`.

```pycon
>>> from datetime import datetime
>>> from decimal import Decimal
>>> import date62

>>> d = '2024-12-29 12:34:56.789012'
>>> dtm = datetime.strptime(d, '%Y-%m-%d %H:%M:%S.%f')

>>> date62.encode(dtm)
'WeCTCYu'

>>> date62.encode(dtm, scut=True, prec=2)
'24CTCYuCj0C'

>>> date62.encode(dtm.date(), scut=True)
'24CT'

>>> date62.encode(dtm.time())
'CYu'

>>> date62.encode(dtm.time(), prec=3)
'CYuCj0C00'

>>> t = '1735468496.789012345678'
>>> date62.encode(Decimal(t), scut=True, prec=4)
'24CTAYuCj0C5ZAw'
```

<!-- docsub: end -->
<!-- docsub: end #usage.md -->


<!-- docsub: begin #cli.md -->
<!-- docsub: include docs/cli.md -->
# CLI Reference

<!-- docsub: begin -->
<!-- docsub: help python -m date62 -->
<!-- docsub: lines after 2 upto -1 -->
<!-- docsub: strip -->
```shell
$ python -m date62 --help
usage: date62 [-h] [--version] {encode,now,time,today} ...

options:
-h, --help            show this help message and exit
--version             show program's version number and exit

subcommands:
{encode,now,time,today}
encode              Encode ISO 8601 datetime string to Date62 format.
now                 Current local datetime in Date62 format.
time                Current local datetime in Date62 format.
today               Current local date in Date62 format.
```
<!-- docsub: end -->

## `date62 encode`

<!-- docsub: begin -->
<!-- docsub: help python -m date62 encode -->
<!-- docsub: lines after 2 upto -1 -->
<!-- docsub: strip -->
```shell
$ date62 parse --help
usage: date62 encode [-h] [-n] [-p INT] text

positional arguments:
text            text containing date or datetime

options:
-h, --help      show this help message and exit
-n, --noscut    do not use shortcut form of Date62
-p, --prec INT  sub-second precision: 1=milli, 2=micro, 3=nano, etc.
```
<!-- docsub: end -->

## `date62 now`

<!-- docsub: begin -->
<!-- docsub: help python -m date62 now -->
<!-- docsub: lines after 2 upto -1 -->
<!-- docsub: strip -->
```shell
$ date62 now --help
usage: date62 now [-h] [-n] [-p INT]

options:
-h, --help      show this help message and exit
-n, --noscut    do not use shortcut form of Date62
-p, --prec INT  sub-second precision: 1=milli, 2=micro, 3=nano, etc.
```
<!-- docsub: end -->

## `date62 time`

<!-- docsub: begin -->
<!-- docsub: help python -m date62 time -->
<!-- docsub: lines after 2 upto -1 -->
<!-- docsub: strip -->
```shell
$ date62 now --help
usage: date62 time [-h] [-p INT]

options:
-h, --help      show this help message and exit
-p, --prec INT  sub-second precision: 1=milli, 2=micro, 3=nano, etc.
```
<!-- docsub: end -->

## `date62 today`

<!-- docsub: begin -->
<!-- docsub: help python -m date62 today -->
<!-- docsub: lines after 2 upto -1 -->
<!-- docsub: strip -->
```shell
$ date62 today --help
usage: date62 today [-h] [-n]

options:
-h, --help    show this help message and exit
-n, --noscut  do not use shortcut form of Date62
```
<!-- docsub: end -->
<!-- docsub: end #cli.md -->


# Contributing

Pull requests, feature requests, and bug reports are welcome!

* [Contribution guidelines](https://github.com/makukha/date62/blob/main/.github/CONTRIBUTING.md)


# Authors

* Michael Makukha


# See also

* [Documentation](https://date62.readthedocs.io)
* [Issues](https://github.com/makukha/date62/issues)
* [Changelog](https://github.com/makukha/date62/blob/main/CHANGELOG.md)
* [Security Policy](https://github.com/makukha/date62/blob/main/.github/SECURITY.md)
* [Contribution Guidelines](https://github.com/makukha/date62/blob/main/.github/CONTRIBUTING.md)
* [Code of Conduct](https://github.com/makukha/date62/blob/main/.github/CODE_OF_CONDUCT.md)
* [License](https://github.com/makukha/date62/blob/main/LICENSE)
