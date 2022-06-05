from KMP_search import KMP_search
from naive_search import naive_search
from KR_search import KR_search

from benchmarks.file_comprehension import turn_file_into_list


with open("benchmarks/pan-tadeusz.txt", 'r', encoding='utf-8') as file:
    pan_tadeusz = turn_file_into_list(file)
    tadeusz_text = ""
    for word in pan_tadeusz:
        tadeusz_text += word
        tadeusz_text += " "



def search(pat, txt):
    M = len(pat)
    N = len(txt)
 
    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0
         
        # For current index i, check
        # for pattern match */
        while(j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1
 
        if (j == M):
            print("Pattern found at index ", i)


def our():
    patterns = pan_tadeusz[:30]
    for pattern in patterns:
        naive_search(pattern, tadeusz_text)

def net():
    patterns = pan_tadeusz[:30]
    for pattern in patterns:
        search(pattern, tadeusz_text)

def test_our(benchmark):
    benchmark(our)

def test_net(benchmark):
    benchmark(net)