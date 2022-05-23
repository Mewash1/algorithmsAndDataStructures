def KR_search(pattern, text, prime_number = 2):
    length = len(text) - len(pattern)
    # stores indexes where pattern is in text
    pattern_in_text = []
    hash_factor = 1
    aphabeth_len = 26
    pattern_hash = 0
    text_hash = 0
    if (length < 0 or len(pattern) == 0 or len(text) == 0):
        return pattern_in_text

    for i in range(len(pattern)):
        pattern_hash = (aphabeth_len * pattern_hash + ord(pattern[i])) % prime_number
        text_hash = (aphabeth_len * text_hash + ord(text[i])) % prime_number
        if i < len(pattern):
            hash_factor = (hash_factor * aphabeth_len) % prime_number

    for i in range(length+1):
        if pattern_hash == text_hash:
            for j in range(len(pattern)):
                pattern_letter = pattern[j]
                try_pattern_letter = text[j+i]
                if pattern_letter != try_pattern_letter:
                    break
            else:
                pattern_in_text.append(i)
        if i < len(text) - len(pattern):
            hash_last_letter = ord(text[i])*hash_factor
            hash_next_letter = ord(text[i+len(pattern)])
            hash_no_last_letter = (text_hash - hash_last_letter)
            text_hash = (aphabeth_len * hash_no_last_letter + hash_next_letter) % prime_number
            if text_hash < 0:
                text_hash += prime_number
    return pattern_in_text
