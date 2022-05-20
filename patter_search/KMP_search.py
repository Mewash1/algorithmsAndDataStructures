def KMP_search(pattern, text):
    pattern_index_in_text = 0
    patterns_in_text = []
    if pattern == '' and text == '':
        return patterns_in_text
    while pattern_index_in_text <= (len(text)) - len(pattern):
        prefix_index = pattern_index_in_text
        prefix_len = 0
        for i in range(len(pattern)):
                pattern_letter = pattern[i]
                text_letter = text[prefix_index]
                if pattern_letter != text_letter:
                    break
                else:
                    prefix_len += 1
                    prefix_index += 1
        else:
            patterns_in_text.append(pattern_index_in_text)
            pattern_index_in_text += 1
            continue
        prefix = text[pattern_index_in_text:prefix_index]
        pre_su_fix = prefix_search(prefix)
        pattern_try_letter = pattern[pre_su_fix]

        # Cheking next letter of the pattern, after a "prefix move",
        # with last not matching letter of the text
        while pattern_try_letter != text_letter and pre_su_fix > 0:
            prefix = pattern[:pre_su_fix]
            pre_su_fix = prefix_search(prefix)
            pattern_try_letter = pattern[pre_su_fix]


        pattern_index_in_text += prefix_len - pre_su_fix


    return patterns_in_text


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





