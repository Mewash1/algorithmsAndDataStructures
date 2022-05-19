from naive_search import naive_search


def test_empty_strings():
    pattern = ''
    text = ''
    assert naive_search(pattern, text) == (False, [])


def test_text_equal_to_pattern():
    pattern = 'aaa'
    text = 'aaa'
    assert naive_search(pattern, text) == (True, [0])


def test_patter_longer_than_text():
    pattern = 'aaasdafas'
    text = 'aaa'
    assert naive_search(pattern, text) == (False, [])


def test_text_longer_than_pattern():
    pattern = 'aaa'
    text = 'aaaaaa'
    assert naive_search(pattern, text) == (True, [0, 1, 2, 3])

