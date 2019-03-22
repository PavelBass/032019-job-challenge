import random
from collections import deque
from typing import (
    Iterable,
    List,
    Tuple,
    Optional,
)

from logging import getLogger

from sibur_markov.utils import normalize_result

logger = getLogger('MarkovChain')


class TextMarkovChain:
    def __init__(self, length=1):
        self.__length = length
        self._words_vocabulary = Dictogram()
        self._ngramms_vocabulary = Vocabulary()
        self.__last_ngramm = deque(maxlen=length)

    def update(self, iterable: Iterable[str]) -> None:
        for word in iterable:
            self._words_vocabulary.add(word)
            if len(self.__last_ngramm) < self.__length:
                self.__last_ngramm.append(word)
                continue
            self._ngramms_vocabulary[tuple(self.__last_ngramm)] += word
            self.__last_ngramm.append(word)

    def get_ngrams(self):
        return self._ngramms_vocabulary.ngrams

    def get_ngrams_statistic(self):
        return self._ngramms_vocabulary.get_ngrams_statistic()

    def generate(self, length):
        logger.debug('=== GENERATION === ')
        result = self._generate_words(self.__length if self.__length < length else length)
        logger.debug('First words: %s', result)
        while len(result) < length:
            word = self._ngramms_vocabulary[tuple(result[-self.__length:])].random_word()
            logger.debug('For ngram %s generated word: %s', str(tuple(result[-self.__length:])), word)
            if not word:
                word = self._generate_words(1)[0]
                logger.debug('Random word: %s', word)
            result.append(word)
        logger.debug('=== GENERATION FINISHED === ')
        return ' '.join(normalize_result(result))

    def _generate_words(self, length):
        return [self._words_vocabulary.random_word() for _ in range(length)]


class Dictogram:
    def __init__(self):
        self.__data = dict()

    def __iadd__(self, other) -> None:
        if not isinstance(other, str):
            raise ValueError('Can only add words (strings)')
        self.add(other)

    def add(self, item):
        if item not in self.__data:
            self.__data[item] = 0
        self.__data[item] += 1

    def get_weighted_words(self):
        return sorted(self.__data.items(), key=lambda x: x[1])

    def random_word(self) -> Optional[str]:
        values_sum = sum(self.__data.values())
        if not values_sum:
            return
        some_value = random.randint(0, values_sum - 1)
        for item, value in self.__data.items():
            some_value -= value
            if some_value <= 0:
                return item


class Vocabulary:
    def __init__(self):
        self.__data = dict()

    def __getitem__(self, item) -> Dictogram:
        if item not in self.__data:
            self.__data[item] = Dictogram()
        return self.__data[item]

    def __setitem__(self, key, value) -> None:
        if key not in self.__data:
            self.__data[key] = Dictogram()

    @property
    def ngrams(self) -> List[Tuple[str]]:
        return list(self.__data.keys())

    def get_ngrams_statistic(self):
        return {
            ' '.join(key): value.get_weighted_words() for key, value in self.__data.items()
        }
