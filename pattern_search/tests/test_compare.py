from KMP_search import KMP_search
from naive_search import naive_search
from KR_search import KR_search
import random

def random_text():
    text = ''
    for _ in range(random.randint(15, 40)):
        if random.randint(0, 1) == 0:
            text += 'a'
        else:
            text += 'b'
    return text


def random_pattern():
    pattern = ''
    for _ in range(random.randint(5, 10)):
        if random.randint(0, 1) == 0:
            pattern += 'a'
        else:
            pattern += 'b'
    return pattern


def test_compare():
    pattern, text = '', ''
    for _ in range(3000):
        text = random_text()
        pattern = random_pattern()
        N_list = naive_search(pattern, text)
        KR_list = KR_search(pattern, text, 2, 2)
        KMP_list = KMP_search(pattern, text)
        assert N_list == KR_list
        assert N_list == KMP_list
        assert KR_list == KMP_list