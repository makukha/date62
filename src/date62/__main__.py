from argparse import ArgumentParser, Namespace  # noqa: F401 # needed for typing
from contextlib import nullcontext as n
from datetime import datetime
import os
import sys

try:
    from typing import Optional, TextIO  # noqa: F401 # needed for typing
except ImportError:
    pass

from . import __version__
import date62


# commands


def cmd_encode(args):  # type: (Namespace) -> None
    """
    Encode ISO 8601 datetime string to Date62 format.
    """
    try:
        value = datetime.fromisoformat(args.text)
    except AttributeError:
        print('This command requires newer Python version.')
        sys.exit(1)
    except ValueError:
        print('Invalid input does not contain date or date-time.')
        sys.exit(1)
    ret = date62.encode(value, args.prec, scut=not args.noscut)
    args.stdout.write(ret + os.linesep)


def cmd_now(args):  # type: (Namespace) -> None
    """
    Current local datetime in Date62 format.
    """
    ret = date62.now(prec=args.prec, scut=not args.noscut)
    args.stdout.write(ret + os.linesep)


def cmd_time(args):  # type: (Namespace) -> None
    """
    Current local datetime in Date62 format.
    """
    ret = date62.encode_time(datetime.now().time(), prec=args.prec)
    args.stdout.write(ret + os.linesep)


def cmd_today(args):  # type: (Namespace) -> None
    """
    Current local date in Date62 format.
    """
    ret = date62.today(scut=not args.noscut)
    args.stdout.write(ret + os.linesep)


# parser


parser = ArgumentParser(prog='date62')
parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)
sub = parser.add_subparsers(title='subcommands')


def add_precision_option(p):  # type: (ArgumentParser) -> None
    p.add_argument(
        '-p',
        '--prec',
        type=int,
        default=0,
        metavar='INT',
        help='sub-second precision: 1=milli, 2=micro, 3=nano, etc.',
    )


def add_no_shortcut_option(p):  # type: (ArgumentParser) -> None
    p.add_argument(
        '-n',
        '--noscut',
        default=False,
        action='store_true',
        help='do not use shortcut form of Date62',
    )


with n(sub.add_parser('encode', help=cmd_encode.__doc__)) as p:
    add_no_shortcut_option(p)
    add_precision_option(p)
    p.add_argument('text', type=str, help='text containing date or datetime')
    p.set_defaults(cmd=cmd_encode)

with n(sub.add_parser('now', help=cmd_now.__doc__)) as p:
    add_no_shortcut_option(p)
    add_precision_option(p)
    p.set_defaults(cmd=cmd_now)

with n(sub.add_parser('time', help=cmd_time.__doc__)) as p:
    add_precision_option(p)
    p.set_defaults(cmd=cmd_time)

with n(sub.add_parser('today', help=cmd_today.__doc__)) as p:
    add_no_shortcut_option(p)
    p.set_defaults(cmd=cmd_today)


# entrypoint


def cli(argv=None, stdout=sys.stdout):  # type: (Optional[list[str]], TextIO) -> int
    args = parser.parse_args(argv)
    args.stdout = stdout
    args.cmd(args)
    return 0


if __name__ == '__main__':
    sys.exit(cli())
