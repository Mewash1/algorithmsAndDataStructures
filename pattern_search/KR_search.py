def KR_search(pattern, text, prime_number = 577 , alphabeth_len = 256):
    length = len(text) - len(pattern)
    # stores indexes where pattern is in text
    pattern_in_text = []
    if (length < 0 or len(pattern) == 0 or len(text) == 0):
        return pattern_in_text

    pattern_hash, text_hash, hash_factor = hash_start(pattern, text,
                                                      prime_number, alphabeth_len)

    for i in range(length+1):
        if pattern_hash == text_hash:
            window_begin = i
            window_end = len(pattern) + i
            try_pattern = text[window_begin:window_end]

            if try_pattern == pattern:
                pattern_in_text.append(i)

        if i < len(text) - len(pattern):
            text_hash = hash_next(pattern, text, prime_number, text_hash,
                                  alphabeth_len, hash_factor, i)
    return pattern_in_text


def hash_start(pattern, text, prime_number, alphabeth_len):
    pattern_hash = 0
    text_hash = 0
    hash_factor = 1
    for i in range(len(pattern)):
        pattern_hash = (alphabeth_len * pattern_hash + ord(pattern[i])) % prime_number
        text_hash = (alphabeth_len * text_hash + ord(text[i])) % prime_number
        if i < len(pattern):
            hash_factor = (hash_factor * alphabeth_len) % prime_number
    return pattern_hash, text_hash, hash_factor


def hash_next(pattern, text, prime_number, alphabeth_len, hash_factor, text_hash, index):

    hash_last_letter = ord(text[index])*hash_factor
    hash_next_letter = ord(text[index+len(pattern)])
    hash_no_last_letter = (text_hash - hash_last_letter)
    text_hash = (alphabeth_len * hash_no_last_letter + hash_next_letter) % prime_number
    if text_hash < 0:
        text_hash += prime_number
    return text_hash
