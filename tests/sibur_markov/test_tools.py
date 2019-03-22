import pytest

from sibur_markov.tools import TextParser


@pytest.mark.parametrize('text,expected', [
    # simple
    ('ааа', ['ааа']),
    # whitespaces
    ('а аа ааа   иии      ыыы', ['а', 'аа', 'ааа', 'иии', 'ыыы']),
    # case insensitive
    ('А аА аАа   иИи      ЫыЫ', ['а', 'аа', 'ааа', 'иии', 'ыыы']),
    # punctuations and whitespaces
    ('а,аа, ааа,', ['а', ',', 'аа', ',', 'ааа', ',']),
    # repeated punctuation as single
    ('а,.аа,... ааа,,,,....', ['а', ',', '.', 'аа', ',', '.', 'ааа', ',', '.']),
    # trash symbols
    ('а,!@!#.аа,..!@#.@$$#$$ @#$#$ %sadf ааа,,,,....pew pew pew', ['а', ',', '.', 'аа', ',', '.', 'ааа', ',', '.']),
])
def test_parser__parse_returns_expected(text, expected):
    # arrange
    parser = TextParser()

    # act
    result = parser.parse(text)

    # assert
    assert list(result) == expected
