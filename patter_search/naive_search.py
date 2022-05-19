from typing import Tuple


def naive_search(pattern, text) -> Tuple[bool, list]:
    length = len(text) - len(pattern)
    found = False
    # stores indexes where pattern is in text
    pattern_in_text = []
    if (length < 0 or
       (len(pattern) == 0 and len(text) == 0)):
        return found, pattern_in_text
    for i in range(length+1):
        try_pattern = text[i:len(pattern)+i]
        if try_pattern == pattern:
            found = True
            pattern_in_text.append(i)
    if found:
        return found, pattern_in_text
    else:
        return found, pattern_in_text
