from morse import translate
import io

def test_one_word():
    new_string = io.StringIO("abc")
    assert translate(new_string) == ".- -... -.-."

def test_two_words():
    new_string = io.StringIO("abc abc")
    assert translate(new_string) == ".- -... -.-. / .- -... -.-."

def test_two_lines():
    new_string = io.StringIO("abc\nabc")
    assert translate(new_string) == ".- -... -.-.\n.- -... -.-."

def test_non_letter_characters():
    new_string = io.StringIO("a34343b3465c 2323 545a998b00c")
    assert translate(new_string) == ".- -... -.-. / .- -... -.-."