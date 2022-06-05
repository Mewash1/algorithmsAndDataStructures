from typing import Tuple


def naive_search(pattern, text) -> Tuple[bool, list]:
    length = len(text) - len(pattern)
    check = True
    # stores indexes where pattern is in text
    pattern_in_text = []
    if (length < 0 or len(pattern) == 0 or len(text) == 0):
        return pattern_in_text
    for i in range(length+1):
        try_pattern = text[i:len(pattern)+i]
        if try_pattern == pattern:
            pattern_in_text.append(i)
        check = True
    return pattern_in_text
