from KR_search import (
    prefix_search,
    prefix_pattern,
    KR_search
)


def test_prefix_search():
    prefix = 'abccab'
    assert prefix_search(prefix) == 2
    prefix = 'abcefefabce'
    assert prefix_search(prefix) == 4


def test_KR_search_easy():
    text = 'tralalatralatytrala'
    pattern = 'alal'
    mathes = KR_search(pattern, text)