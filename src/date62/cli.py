from datetime import date, datetime

import dateutil.parser

try:
    import rich_click as click
except ImportError:
    import click  # type: ignore[no-redef]

from . import __version__, to_date62


@click.group()
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx: click.Context) -> None:
    ctx.show_default = True


precision_option = click.option(
    '-p',
    '--precision',
    type=int,
    default=0,
    metavar='INT',
    help='Sub-second precision, power of 1000: 1=millisec, 2=microsec, 3=nanosec, etc.',
)
shortcut_option = click.option(
    '-n/ ',
    '--no-shortcut',
    is_flag=True,
    default=False,
    help='Do not use shortcut form.',
)


@cli.command()
@shortcut_option
def today(no_shortcut: bool) -> None:
    """
    Current local date in Date62 format.
    """
    ret = to_date62(date.today(), shortcut=not no_shortcut)
    click.echo(ret)


@cli.command()
@precision_option
@shortcut_option
def now(precision: int, no_shortcut: bool) -> None:
    """
    Current local datetime in Date62 format.
    """
    ret = to_date62(datetime.now(), precision=precision, shortcut=not no_shortcut)
    click.echo(ret)


@cli.command()
@precision_option
@shortcut_option
@click.argument('text', type=str)
def parse(text: str, precision: int, no_shortcut: bool) -> None:
    """
    Parse any dateutil-readable string to Date62 format.
    """
    ret = to_date62(
        dateutil.parser.parse(text),
        shortcut=not no_shortcut,
        precision=precision,
    )
    click.echo(ret)
