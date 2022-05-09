import random, pytest, json, copy
from ..d_ary_heap import Heap
with open("list.json", 'r') as file:
    random_list = json.load(file)


def pop_top(n, num_children):
    heap = Heap(num_children, random_list.copy())
    for _ in range(n):
        heap.pop()

def test_benchmark_pop_2_ary_heap_10000(benchmark):
    
    benchmark.pedantic(pop_top, args=(10000, 2))

def test_benchmark_pop_2_ary_heap_20000(benchmark):
    
    benchmark.pedantic(pop_top, args=(20000, 2))

def test_benchmark_pop_2_ary_heap_30000(benchmark):
    
    benchmark.pedantic(pop_top, args=(30000, 2))

def test_benchmark_pop_2_ary_heap_40000(benchmark):
    
    benchmark.pedantic(pop_top, args=(40000, 2))

def test_benchmark_pop_2_ary_heap_50000(benchmark):
    
    benchmark.pedantic(pop_top, args=(50000, 2))

def test_benchmark_pop_2_ary_heap_60000(benchmark):
    
    benchmark.pedantic(pop_top, args=(60000, 2))

def test_benchmark_pop_2_ary_heap_70000(benchmark):
    
    benchmark.pedantic(pop_top, args=(70000, 2))

def test_benchmark_pop_2_ary_heap_80000(benchmark):
    
    benchmark.pedantic(pop_top, args=(80000, 2))

def test_benchmark_pop_2_ary_heap_90000(benchmark):
    
    benchmark.pedantic(pop_top, args=(90000, 2))

def test_benchmark_pop_2_ary_heap_100000(benchmark):
    
    benchmark.pedantic(pop_top, args=(100000, 2))


def test_benchmark_pop_3_ary_heap_10000(benchmark):
    
    benchmark.pedantic(pop_top, args=(10000, 3))

def test_benchmark_pop_3_ary_heap_20000(benchmark):
    
    benchmark.pedantic(pop_top, args=(20000, 3))

def test_benchmark_pop_3_ary_heap_30000(benchmark):
        
    benchmark.pedantic(pop_top, args=(30000, 3))

def test_benchmark_pop_3_ary_heap_40000(benchmark):
    
    benchmark.pedantic(pop_top, args=(40000, 3))

def test_benchmark_pop_3_ary_heap_50000(benchmark):
    
    benchmark.pedantic(pop_top, args=(50000, 3))

def test_benchmark_pop_3_ary_heap_60000(benchmark):
    
    benchmark.pedantic(pop_top, args=(60000, 3))

def test_benchmark_pop_3_ary_heap_70000(benchmark):
    
    benchmark.pedantic(pop_top, args=(70000, 3))

def test_benchmark_pop_3_ary_heap_80000(benchmark):
    
    benchmark.pedantic(pop_top, args=(80000, 3))

def test_benchmark_pop_3_ary_heap_90000(benchmark):
    
    benchmark.pedantic(pop_top, args=(90000, 3))

def test_benchmark_pop_3_ary_heap_100000(benchmark):
    
    benchmark.pedantic(pop_top, args=(100000, 3))


def test_benchmark_pop_4_ary_heap_10000(benchmark):
    
    benchmark.pedantic(pop_top, args=(10000, 4))

def test_benchmark_pop_4_ary_heap_20000(benchmark):
    
    benchmark.pedantic(pop_top, args=(20000, 4))

def test_benchmark_pop_4_ary_heap_30000(benchmark):
    
    benchmark.pedantic(pop_top, args=(30000, 4))

def test_benchmark_pop_4_ary_heap_40000(benchmark):
    
    benchmark.pedantic(pop_top, args=(40000, 4))

def test_benchmark_pop_4_ary_heap_50000(benchmark):
    
    benchmark.pedantic(pop_top, args=(50000, 4))

def test_benchmark_pop_4_ary_heap_60000(benchmark):
    
    benchmark.pedantic(pop_top, args=(60000, 4))

def test_benchmark_pop_4_ary_heap_70000(benchmark):
    
    benchmark.pedantic(pop_top, args=(70000, 4))

def test_benchmark_pop_4_ary_heap_80000(benchmark):
    
    benchmark.pedantic(pop_top, args=(80000, 4))

def test_benchmark_pop_4_ary_heap_90000(benchmark):
    
    benchmark.pedantic(pop_top, args=(90000, 4))

def test_benchmark_pop_4_ary_heap_100000(benchmark):
        
    benchmark.pedantic(pop_top, args=(100000, 4))