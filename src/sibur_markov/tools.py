from typing import Iterable

from sibur_markov import constants


class TextParser:
    def __init__(self):
        self._text = ''
        self._position = 0
        self._last_word = ''
        self._letters = set(constants.LOWER_LETTERS)
        self._punctuation_words = set(constants.PUNCTUATION_WORDS)
        self._parsed = []

    def _set_defaults(self) -> None:
        self._text = ''
        self._position = 0
        self._last_word = ''
        self._letters = set(constants.LOWER_LETTERS)
        self._punctuation_words = set(constants.PUNCTUATION_WORDS)
        self._parsed = []

    @property
    def parsed(self) -> Iterable[str]:
        return iter(self._parsed)

    def parse(self, text: str) -> Iterable[str]:
        self._set_defaults()
        self._text = text

        while self._position < len(self._text):
            if self._text[self._position].lower() in self._letters:
                self._get_next_word()
            elif self._text[self._position].lower() in self._punctuation_words:
                self._get_next_punctuation_word()
            else:
                self._position += 1
        return self.parsed

    def _get_next_word(self) -> None:
        self._last_word = ''
        while self._position < len(self._text):
            letter = self._text[self._position].lower()
            if letter not in self._letters:
                break
            self._last_word += letter
            self._position += 1
        if self._last_word:
            self._parsed.append(self._last_word)

    def _get_next_punctuation_word(self) -> None:
        while self._position < len(self._text):
            punctuation_word = self._text[self._position].lower()
            if punctuation_word not in self._punctuation_words:
                break
            elif punctuation_word == self._last_word:
                self._position += 1
                continue
            self._last_word = punctuation_word
            self._parsed.append(self._last_word)
            self._position += 1
