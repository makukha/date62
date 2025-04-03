import argparse
from datetime import datetime
import os
import sys

try:
    from typing import Optional, TextIO  # noqa: F401 # needed for typing
except ImportError:
    pass

from . import __version__
import date62


class ArgumentParser(argparse.ArgumentParser):
    def __enter__(self):  # type: () -> ArgumentParser
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # type: (type, object, object) -> None
        pass


# commands


def cmd_encode(args):  # type: (argparse.Namespace) -> None
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
    ret = date62.encode(value, args.prec, shortcut=not args.noshort)
    args.stdout.write(ret + os.linesep)


def cmd_now(args):  # type: (argparse.Namespace) -> None
    """
    Current local datetime in Date62 format.
    """
    ret = date62.now(prec=args.prec, shortcut=not args.noshort)
    args.stdout.write(ret + os.linesep)


def cmd_today(args):  # type: (argparse.Namespace) -> None
    """
    Current local date in Date62 format.
    """
    ret = date62.today(shortcut=not args.noshort)
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
        '--noshort',
        default=False,
        action='store_true',
        help='do not use shortcut form of Date62',
    )


with sub.add_parser('encode', help=cmd_encode.__doc__) as cmd:
    add_no_shortcut_option(cmd)
    add_precision_option(cmd)
    cmd.add_argument('text', type=str, help='text containing date or datetime')
    cmd.set_defaults(cmd=cmd_encode)

with sub.add_parser('now', help=cmd_now.__doc__) as cmd:
    add_no_shortcut_option(cmd)
    add_precision_option(cmd)
    cmd.set_defaults(cmd=cmd_now)

with sub.add_parser('today', help=cmd_today.__doc__) as cmd:
    add_no_shortcut_option(cmd)
    cmd.set_defaults(cmd=cmd_today)


# entrypoint


def cli(argv=None, stdout=sys.stdout):  # type: (Optional[list[str]], TextIO) -> int
    args = parser.parse_args(argv)
    args.stdout = stdout
    args.cmd(args)
    return 0


if __name__ == '__main__':
    sys.exit(cli())
