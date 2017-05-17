"""
Tests for trigrams
"""
import pytest

PARAMS_TABLE = [
    ('I wish I may I wish I might', {
        'I wish': ['I', 'I'],
        'wish I': ['may', 'might'],
        'may I': ['wish'],
        'I may':['I']
        })
        ]
REMOVE_PUNCTUATION_PARAMS_TABLE = [
    ('I wish, I may, I wish, I might.\n', 'I wish I may I wish I might'),
    ('\nI came, I saw\n, I conquered.', 'I came I saw I conquered')]


@pytest.mark.parametrize('text, result', PARAMS_TABLE)
def test_create_trigrams(text, result):
    from trigrams import create_trigrams
    assert create_trigrams(text) == result


@pytest.mark.parametrize('text, result', REMOVE_PUNCTUATION_PARAMS_TABLE)
def test_remove_punctuation(text, result):
    from trigrams import remove_punctuation
    assert remove_punctuation(text) == result
