from typing import Tuple


def naive_search(pattern, text) -> Tuple[bool, list]:
    length = len(text) - len(pattern)
    # stores indexes where pattern is in text
    pattern_in_text = []
    if (length < 0 or
       (len(pattern) == 0 and len(text) == 0)):
        return pattern_in_text
    for i in range(length+1):
        try_pattern = text[i:len(pattern)+i]
        for j in range(len(pattern)):
            pattern_letter = pattern[j]
            try_pattern_letter = try_pattern[j]
            if pattern_letter != try_pattern_letter:
                break
        else:
            pattern_in_text.append(i)
    return pattern_in_text
