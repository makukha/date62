from datetime import date, datetime

from dateutil.parser import parse
try:
    import rich_click as click
except ImportError:
    import click

from . import __version__, to_date62


@click.group()
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx):
    pass


no_shortcut_name = ('-n/ ', '--no-shortcut')
no_shortcut_args = dict(
    is_flag=True, default=False, show_default=True,
    help='Don\'t use shortcut form.',
)


@cli.command()
@click.option(*no_shortcut_name, **no_shortcut_args)
def today(no_shortcut: bool):
    """
    Current local date in Date62 format.
    """
    ret = to_date62(date.today(), shortcut=not no_shortcut)
    print(ret)


@cli.command()
@click.option(*no_shortcut_name, **no_shortcut_args)
@click.option(
    '-p', '--precision', type=int, default=0,
    metavar='INT', show_default=True,
    help='Sub-second precision as power of 10**3: 1=milli, 2=micro, 3=nano, etc.',
)
def now(precision: int, no_shortcut: bool):
    """
    Current local datetime in Date62 format.
    """
    ret = to_date62(datetime.now(), precision=precision, shortcut=not no_shortcut)
    print(ret)


@cli.command()
@click.option(*no_shortcut_name, **no_shortcut_args)
@click.option(
    '-p', '--precision', type=int, default=0,
    metavar='INT', show_default=True,
    help='Sub-second precision as power of 10**3: 1=milli, 2=micro, 3=nano, etc.',
)
@click.option(
    '-s', '--subsec', type=int, default=0,
    metavar='INT', show_default=True,
    help='Append sub-seconds as integer between 0 and 10**3**precision.',
)
@click.argument(
    'text', type=str,
)
def parse(text: str, precision: int, subsec: int, no_shortcut: bool):
    """
    Parse any dateutil-readable datetime to Date62 format.
    """
    ret = to_date62(
        parse(text),
        shortcut=not no_shortcut,
        precision=precision,
        subsec=subsec,
    )
    print(ret)
