def KR_search(pattern, text):
    pattern_index_in_text = 0
    patterns_in_text = []
    found = False
    prefix_index = 0
    while pattern_index_in_text != (len(text) - 1):
        patterns_in_text, found = prefix_pattern(pattern, text, pattern_index_in_text,
                                                 patterns_in_text, found)
    return patterns_in_text

def prefix_pattern(pattern, text,
                  pattern_index_in_text, patterns_in_text: list, found) -> bool:
    prefix_index = pattern_index_in_text
    prefix_len = 0
    for i in range(len(pattern)-1):
            pattern_letter = pattern[i]
            text_letter = text[prefix_index]
            if pattern_letter != text_letter:
                break
            else:
                prefix_len += 1
                prefix_index += 1
    else:
        patterns_in_text.append(pattern_index_in_text)
        found = True
        pattern_index_in_text += len(pattern)
        patterns_in_text, found = prefix_pattern(pattern, text, pattern_index_in_text,
                                                 patterns_in_text, found)
    prefix = text[pattern_index_in_text:prefix_index]
    pre_su_fix = prefix_search(prefix)
    pattern_index_in_text += prefix_len - pre_su_fix
    patterns_in_text, found = prefix_pattern(pattern, text, pattern_index_in_text,
                                             patterns_in_text, found)
    return pattern_index_in_text, found


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





