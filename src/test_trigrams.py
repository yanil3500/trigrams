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


@pytest.mark.parametrize('text, result', PARAMS_TABLE)
def test_solutions_trigrams(text, result):
    from trigrams import create_trigrams
    assert create_trigrams(text) == result
