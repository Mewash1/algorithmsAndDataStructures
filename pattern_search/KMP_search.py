def KMP_search(pattern, text):
    prefix_dict = make_prefix_dict(pattern)
    patterns_in_text = []
    if pattern == '' or text == '':
        return patterns_in_text
    prefix = ''
    pre_su_fix = 0
    pattern_start_in_text = 0
    pattern_end_in_text = 0

    while pattern_start_in_text <= (len(text)) - len(pattern):
        for i in range(len(pattern) - pre_su_fix):

                index_in_pattern = pattern_end_in_text - pattern_start_in_text
                pattern_letter = pattern[index_in_pattern]
                text_letter = text[pattern_end_in_text]
                if pattern_letter != text_letter:
                    break
                else:
                    pattern_end_in_text += 1
        else:
            patterns_in_text.append(pattern_start_in_text)
            pattern_start_in_text += 1
            pattern_end_in_text = pattern_start_in_text
            pre_su_fix = 0
            continue

        prefix = text[pattern_start_in_text:pattern_end_in_text]
        pre_su_fix = prefix_dict[prefix]
        prefix_len = len(prefix)

        pattern_start_in_text += prefix_len - pre_su_fix

        if pre_su_fix == -1:
            pattern_end_in_text = pattern_start_in_text
            pre_su_fix = 0

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


def make_prefix_dict(pattern):
    prefix_dict = {}
    prefix_dict[''] = -1
    for i in range(1, len(pattern)+1):
        prefix = pattern[:i]
        outcome = prefix_search(prefix)
        if i < len(pattern):
            wrong_letter = pattern[i]
            match_letter = prefix[outcome]
            if wrong_letter == match_letter:
                if outcome == 0:
                    outcome2 = -1
                else:
                    outcome2 = prefix_dict[prefix[:outcome]]

                outcome = outcome2
        prefix_dict[prefix] = outcome
    return prefix_dict


