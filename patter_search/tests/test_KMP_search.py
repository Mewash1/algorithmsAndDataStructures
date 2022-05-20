from KMP_search import (
    prefix_search,
    KMP_search
)


def test_prefix_search():
    prefix = 'abccab'
    assert prefix_search(prefix) == 2
    prefix = 'abcefefabce'
    assert prefix_search(prefix) == 4


def test_KMP_search_easy():
    text = 'tralalatralatytrala'
    pattern = 'alal'
    mathes = KMP_search(pattern, text)
    assert mathes == [2]


def test_KMP_search_easy2():
    text = 'abababacababacacab'
    pattern = 'abababab'
    mathes = KMP_search(pattern, text)
    assert mathes == []


def test_KMP_search_easy3():
    text = 'abacabacababacacab'
    pattern = 'abacabab'
    mathes = KMP_search(pattern, text)
    assert mathes == [4]


def test_KMP_search_easy4():
    text = 'adacadadacadabacab'
    pattern = 'adacadab'
    mathes = KMP_search(pattern, text)
    assert mathes == [6]


def test_empty_strings():
    pattern = ''
    text = ''
    assert KMP_search(pattern, text) == []


def test_text_equal_to_pattern():
    pattern = 'aaa'
    text = 'aaa'
    assert KMP_search(pattern, text) == [0]


def test_patter_longer_than_text():
    pattern = 'aaasdafas'
    text = 'aaa'
    assert KMP_search(pattern, text) == []


def test_text_longer_than_pattern():
    pattern = 'aaa'
    text = 'aaaaaa'
    assert KMP_search(pattern, text) == [0, 1, 2, 3]