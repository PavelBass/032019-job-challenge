import logging

from pkg_resources import (
    DistributionNotFound,
    get_distribution,
)

__project__ = 'sibur_markov'

try:
    __version__ = get_distribution(__project__).version
except DistributionNotFound:
    __version__ = 'unknown'

VERSION = f'{__project__}_{__version__}'


def setup_logging(level: str = logging.DEBUG) -> None:
    logging.basicConfig(
        level=level,
        format='%(asctime)s %(name)-24s %(levelname)s %(message)s',
        datefmt='%d.%m.%Y[%H:%M:%S]',
    )
