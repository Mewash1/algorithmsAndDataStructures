from KR_search import KR_search


def test_empty_strings():
    pattern = ''
    text = ''
    assert KR_search(pattern, text) == []

def test_empty_text():
    pattern = 'aaa'
    text = ''
    assert KR_search(pattern, text) == []

def test_empty_pattern():
    pattern = ''
    text = 'aaaaa'
    assert KR_search(pattern, text) == []

def test_text_equal_to_pattern():
    pattern = 'aaa'
    text = 'aaa'
    assert KR_search(pattern, text, 1, 2) == [0]

def test_patter_longer_than_text():
    pattern = 'aaasdafas'
    text = 'aaa'
    assert KR_search(pattern, text, 3, 4) == []

def test_text_longer_than_pattern():
    pattern = 'aaa'
    text = 'aaaaaa'
    assert KR_search(pattern, text, 1, 1) == [0, 1, 2, 3]

def test_pattern_not_in_text():
    pattern = 'bbb'
    text = "ababaab"
    assert KR_search(pattern, text, 1, 2) == []
