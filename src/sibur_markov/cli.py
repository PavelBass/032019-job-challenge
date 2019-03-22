import logging

import click
from sibur_markov import setup


logger = logging.getLogger(__name__)


@click.group()
def cli() -> None:
    setup()


@cli.command('generate')
@click.option('-v', '--verbose', is_flag=True, default=False)
@click.argument('source', type=click.File('r'))
@click.argument('result', type=click.File('w'))
@click.argument('line_length', type=click.IntRange(0, 20))
@click.argument('result_length', type=int)
def main(verbose: bool, source: click.File, result: click.File, line_length: int, result_length: int) -> None:
    logger.info('=== START ===')
    logger.info(verbose)
    text = source.read()


cli.add_command(main)
