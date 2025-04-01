# CLI Reference

<!-- docsub: begin -->
<!-- docsub: help python -m date62 -->
<!-- docsub: lines after 2 upto -1 -->
<!-- docsub: strip -->
```shell
$ python -m date62 --help
Usage: python -m date62 [OPTIONS] COMMAND [ARGS]...

╭─ Options ──────────────────────────────────────────────────────────╮
│ --version      Show the version and exit.                          │
│ --help         Show this message and exit.                         │
╰────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────╮
│ now     Current local datetime in Date62 format.                   │
│ parse   Parse any dateutil-readable string to Date62 format.       │
│ today   Current local date in Date62 format.                       │
╰────────────────────────────────────────────────────────────────────╯
```
<!-- docsub: end -->

## `date62 now`

<!-- docsub: begin -->
<!-- docsub: help python -m date62 now -->
<!-- docsub: lines after 2 upto -1 -->
<!-- docsub: strip -->
```shell
$ date62 now --help
Usage: python -m date62 now [OPTIONS]

Current local datetime in Date62 format.

╭─ Options ──────────────────────────────────────────────────────────╮
│ --precision    -p  INT  Sub-second precision, power of 1000:       │
│                         1=millisec, 2=microsec, 3=nanosec, etc.    │
│                         [default: 0]                               │
│ --no-shortcut  -n       Do not use shortcut form.                  │
│ --help                  Show this message and exit.                │
╰────────────────────────────────────────────────────────────────────╯
```
<!-- docsub: end -->

## `date62 today`

<!-- docsub: begin -->
<!-- docsub: help python -m date62 today -->
<!-- docsub: lines after 2 upto -1 -->
<!-- docsub: strip -->
```shell
$ date62 today --help
Usage: python -m date62 today [OPTIONS]

Current local date in Date62 format.

╭─ Options ──────────────────────────────────────────────────────────╮
│ --no-shortcut  -n    Do not use shortcut form.                     │
│ --help               Show this message and exit.                   │
╰────────────────────────────────────────────────────────────────────╯
```
<!-- docsub: end -->


## `date62 parse`

<!-- docsub: begin -->
<!-- docsub: help python -m date62 parse -->
<!-- docsub: lines after 2 upto -1 -->
<!-- docsub: strip -->
```shell
$ date62 parse --help
Usage: python -m date62 parse [OPTIONS] TEXT

Parse any dateutil-readable string to Date62 format.

╭─ Options ──────────────────────────────────────────────────────────╮
│ --precision    -p  INT  Sub-second precision, power of 1000:       │
│                         1=millisec, 2=microsec, 3=nanosec, etc.    │
│                         [default: 0]                               │
│ --no-shortcut  -n       Do not use shortcut form.                  │
│ --help                  Show this message and exit.                │
╰────────────────────────────────────────────────────────────────────╯
```
<!-- docsub: end -->
