import argparse
from morse_table import morse_table

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=str)
    return parser.parse_args()


def check_if_word_right(word):
    for char in word:
        if char.upper() in morse_table:
            return True
    return False


def translate(file):
    morse_string = ""
    for line in file.readlines():
        line = line.split(" ")
        for word in line:
            if not check_if_word_right(word):
                continue
            for char in word:
                try:
                    morse_string += morse_table[char.upper()] + " "
                except KeyError:
                    continue
            morse_string += "/ "
        morse_string = morse_string[:-2]
        morse_string = morse_string.rstrip()
        morse_string += "\n"
    morse_string = morse_string[:-1]
    return morse_string


def main():
    file_path = create_parser().file_path
    with open(file_path, 'r') as file:
        print(translate(file))