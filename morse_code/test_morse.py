from morse_code import translate
import io

def test_one_word(benchmark):
    new_string = io.StringIO("abc")
    assert translate(new_string) == ".- -... -.-."
    benchmark(translate, new_string) 

def test_two_words(benchmark):
    new_string = io.StringIO("abc abc")
    assert translate(new_string) == ".- -... -.-. / .- -... -.-."
    benchmark(translate, new_string) 

def test_two_lines(benchmark):
    new_string = io.StringIO("abc\nabc")
    assert translate(new_string) == ".- -... -.-.\n.- -... -.-."
    benchmark(translate, new_string) 

def test_non_letter_characters(benchmark):
    new_string = io.StringIO("a34343b3465c 2323 545a998b00c")
    assert translate(new_string) == ".- -... -.-. / .- -... -.-."
    benchmark(translate, new_string) 