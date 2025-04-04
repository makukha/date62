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
