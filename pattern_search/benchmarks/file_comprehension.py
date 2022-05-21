def remove_wrong_charaters_from_word(word):
    new_word = ""
    good_charaters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                      'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                      'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                      'ą', 'ę', 'ć', 'ń', 'ł', 'ó', 'ś', 'ż', 'ź'}
    for char in word:
        if char.lower() in good_charaters:
            new_word += char
    return new_word


def turn_file_into_list(file_handle):
    new_list = []
    for line in file_handle.readlines():
        line = line.split(" ")
        for word in line:
            new_word = remove_wrong_charaters_from_word(word)
            if len(new_word) != 0:
                new_list.append(new_word)
    return new_list
