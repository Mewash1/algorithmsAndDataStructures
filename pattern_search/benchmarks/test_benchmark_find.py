from KMP_search import KMP_search
from naive_search import naive_search
from KR_search import KR_search

from .file_comprehension import turn_file_into_list


with open("pan-tadeusz.txt", 'r', encoding='utf-8') as file:
    pan_tadeusz = turn_file_into_list(file)
    tadeusz_text = ""
    for word in pan_tadeusz:
        tadeusz_text += word
        tadeusz_text += " "

def find_n_words(n, type):
    '''
    type:
        0 = naive_search
        1 = KR_search
        2 = KMP_search
    '''
    patterns = pan_tadeusz[:n]
    for pattern in patterns:
        if type == 0:
            naive_search(pattern, tadeusz_text)
        elif type == 1:
            KR_search(pattern, tadeusz_text, 197, 256)
        elif type == 2:
            KMP_search(pattern, tadeusz_text)


def test_benchmark_naive_find_10(benchmark):
    benchmark(find_n_words, 10, 0)

def test_benchmark_naive_find_20(benchmark):
    benchmark(find_n_words, 20, 0)

def test_benchmark_naive_find_30(benchmark):
    benchmark(find_n_words, 30, 0)

def test_benchmark_naive_find_40(benchmark):
    benchmark(find_n_words, 40, 0)

def test_benchmark_naive_find_50(benchmark):
    benchmark(find_n_words, 50, 0)

def test_benchmark_naive_find_60(benchmark):
    benchmark(find_n_words, 60, 0)

def test_benchmark_naive_find_70(benchmark):
    benchmark(find_n_words, 70, 0)

def test_benchmark_naive_find_80(benchmark):
    benchmark(find_n_words, 80, 0)

def test_benchmark_naive_find_90(benchmark):
    benchmark(find_n_words, 90, 0)

def test_benchmark_naive_find_100(benchmark):
    benchmark(find_n_words, 100, 0)



def test_benchmark_KR_find_10(benchmark):
    benchmark(find_n_words, 10, 1)

def test_benchmark_KR_find_20(benchmark):
    benchmark(find_n_words, 20, 1)

def test_benchmark_KR_find_30(benchmark):
    benchmark(find_n_words, 30, 1)

def test_benchmark_KR_find_40(benchmark):
    benchmark(find_n_words, 40, 1)

def test_benchmark_KR_find_50(benchmark):
    benchmark(find_n_words, 50, 1)

def test_benchmark_KR_find_60(benchmark):
    benchmark(find_n_words, 60, 1)

def test_benchmark_KR_find_70(benchmark):
    benchmark(find_n_words, 70, 1)

def test_benchmark_KR_find_80(benchmark):
    benchmark(find_n_words, 80, 1)

def test_benchmark_KR_find_90(benchmark):
    benchmark(find_n_words, 90, 1)

def test_benchmark_KR_find_100(benchmark):
    benchmark(find_n_words, 100, 1)




def test_benchmark_KMP_find_10(benchmark):
    benchmark(find_n_words, 10, 2)

def test_benchmark_KMP_find_20(benchmark):
    benchmark(find_n_words, 20, 2)

def test_benchmark_KMP_find_30(benchmark):
    benchmark(find_n_words, 30, 2)

def test_benchmark_KMP_find_40(benchmark):
    benchmark(find_n_words, 40, 2)

def test_benchmark_KMP_find_50(benchmark):
    benchmark(find_n_words, 50, 2)

def test_benchmark_KMP_find_60(benchmark):
    benchmark(find_n_words, 60, 2)

def test_benchmark_KMP_find_70(benchmark):
    benchmark(find_n_words, 70, 2)

def test_benchmark_KMP_find_80(benchmark):
    benchmark(find_n_words, 80, 2)

def test_benchmark_KMP_find_90(benchmark):
    benchmark(find_n_words, 90, 2)

def test_benchmark_KMP_find_100(benchmark):
    benchmark(find_n_words, 100, 2)