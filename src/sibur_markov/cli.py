import logging
import os
from random import randint

import click

from sibur_markov import setup_logging
from sibur_markov.markov import TextMarkovChain
from sibur_markov.tools import TextParser

logger = logging.getLogger(__name__)


@click.group()
def cli() -> None:
    pass


@cli.command('generate')
@click.option('-v', '--verbose', is_flag=True, default=False)
@click.argument('source', type=click.File('r'))
@click.argument('result', type=click.File('w'))
@click.argument('line_length', type=click.IntRange(1, 20))
@click.argument('result_length', type=int)
def main(verbose: bool, source: click.File, result: click.File, line_length: int, result_length: int) -> None:
    setup_logging(logging.DEBUG if verbose else logging.INFO)
    logger.info('== Start ==')
    parser = TextParser()
    parser.parse(source.read())
    logger.info('Parsed text from %s', source.name)

    markov_chain = TextMarkovChain(line_length)
    markov_chain.update(parser.parsed)

    result.write(markov_chain.generate(result_length))
    logger.info('Generation result written to %s', result.name)
    logger.info('== Finish ==')


@cli.command('test_generation')
@click.argument('line_length', type=click.IntRange(1, 3), default=2)
def test(line_length):
    setup_logging(logging.DEBUG)
    logger.info('=== START TEST GENERATION ===')
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    with open(os.path.join(base_dir, 'test_source.txt'), 'r') as file:
        text = file.read()
    logger.info('Text: %s', text)
    parser = TextParser()
    parser.parse(text)
    logger.info('Parsed: %s', list(parser.parsed))

    logger.info('Set line_length=%d', line_length)

    result_length = randint(10, 30)
    logger.info('Set result_length=%d', result_length)

    markov_chain = TextMarkovChain(length=line_length)
    markov_chain.update(parser.parsed)

    logger.info('Ngrams: %s', markov_chain.get_ngrams())
    logger.info('Ngrams statistic: %s', markov_chain.get_ngrams_statistic())

    logger.info('Generated: %s', markov_chain.generate(result_length))


cli.add_command(main)
cli.add_command(test)
