import pytest

from sibur_markov.utils import normalize_result


@pytest.mark.parametrize('result,expected', [
    # simple
    (['ааа', 'bbb'], ['ааа', 'bbb']),
    # punctuations added to words
    (['ааа', ',', 'bbb', '.'], ['ааа,', 'bbb.']),
    # words capitalization
    (['ааа', '.', 'bbb'], ['ааа.', 'Bbb']),

])
def test_parser__parse_returns_expected(result, expected):
    # arrange, act
    normalized = list(normalize_result(result))

    # assert
    assert normalized == expected
