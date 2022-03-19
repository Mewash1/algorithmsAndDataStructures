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


def translate(file_path):
    morse_string = ""
    with open(file_path, 'r') as file:
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
            morse_string += "\n"
    return morse_string


def main():
    # file_path = create_parser().file_path
    file_path = "/home/miloszun/AISDI/aisdi/morse_code/plik.txt"
    print(translate(file_path))

main()