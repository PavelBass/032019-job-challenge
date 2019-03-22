import pytest

from sibur_markov.utils import normalize_result


@pytest.mark.parametrize('result,expected', [
    # simple
    (['aaa', 'bbb'], ['Aaa', 'bbb.']),
    # punctuations added to words
    (['aaa', ',', 'bbb', '.'], ['Aaa,', 'bbb.']),
    # words capitalization
    (['aaa', '.', 'bbb'], ['Aaa.', 'Bbb.']),

])
def test_parser__parse_returns_expected(result, expected):
    # arrange, act
    normalized = list(normalize_result(result))

    # assert
    assert normalized == expected
