from typing import (
    List,
    Generator,
)

from sibur_markov import constants


def normalize_result(result: List[str]) -> Generator[None, str, None]:
    position = 0
    is_last_word_punctuation = True
    is_last_punctuation_dot = True
    while position < len(result):
        word = result[position]
        if word in constants.PUNCTUATION_WORDS:
            is_last_punctuation_dot = word == constants.DOT
            if is_last_word_punctuation:
                position += 1
                continue
            is_last_word_punctuation = True
        else:
            if is_last_word_punctuation and is_last_punctuation_dot:
                word = word.capitalize()
            is_last_word_punctuation = False

        if position + 1 < len(result) and result[position + 1] in constants.PUNCTUATION_WORDS:
            word += result[position + 1]
            is_last_word_punctuation = True
            is_last_punctuation_dot = result[position + 1] == constants.DOT
            position += 1
        elif position + 1 == len(result):
            word += constants.DOT
        yield word
        position += 1
