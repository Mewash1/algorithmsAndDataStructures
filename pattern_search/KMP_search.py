def KMP_search(pattern, text):
    found_patterns = []
    if pattern == '' or text == '':
        return found_patterns
    pattern_len = len(pattern)
    text_len = len(text)
    prefix_dict = make_prefix_dict(pattern)
    index_txt = 0
    index_pattern = 0
    while index_txt < text_len:
        if pattern[index_pattern] == text[index_txt]:
            index_txt += 1
            index_pattern += 1

        if index_pattern == pattern_len:
            found_pattern = index_txt - index_pattern
            found_patterns.append(found_pattern)
            index_pattern = prefix_dict[index_pattern]
        elif index_txt < text_len and pattern[index_pattern] != text[index_txt]:
            if index_pattern != 0:
                index_pattern = prefix_dict[index_pattern]
            else:
                index_txt += 1
    return found_patterns


def prefix_search(pattern) -> int:
    if len(pattern) == 0:
        return -1
    id1 = 0
    id2 = len(pattern) - 1
    while id2 != 0:
        id1 += 1
        prefix = pattern[:id2]
        sufix = pattern[id1:]
        if prefix == sufix:
            return len(prefix)
        id2 -= 1
    return 0


def make_prefix_dict(pattern):
    prefix_dict = {}
    prefix_dict[0] = 0
    for i in range(1, len(pattern)+1):
        prefix = pattern[:i]
        outcome = prefix_search(prefix)
        prefix_dict[i] = outcome
    return prefix_dict


