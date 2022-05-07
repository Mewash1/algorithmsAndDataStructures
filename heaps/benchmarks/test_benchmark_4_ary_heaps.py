import random, pytest
from ..d_ary_heap import Heap

@pytest.fixture
def random_list():
    random_list = []
    for _ in range(10000):
        random_list.append(random.randint(1, 30000))
    return random_list

def create_heap(rlist):
    Heap(4, rlist)

def pop_top(heap, n):
    for _ in range(n):
        heap.pop()

def test_benchmark_create_4_ary_heap_10000(benchmark, random_list):
    benchmark(create_heap, random_list[:10000])

def test_benchmark_create_4_ary_heap_20000(benchmark, random_list):
    benchmark(create_heap, random_list[:20000])

def test_benchmark_create_4_ary_heap_30000(benchmark, random_list):
    benchmark(create_heap, random_list[:30000])

def test_benchmark_create_4_ary_heap_40000(benchmark, random_list):
    benchmark(create_heap, random_list[:40000])

def test_benchmark_create_4_ary_heap_50000(benchmark, random_list):
    benchmark(create_heap, random_list[:50000])

def test_benchmark_create_4_ary_heap_60000(benchmark, random_list):
    benchmark(create_heap, random_list[:60000])

def test_benchmark_create_4_ary_heap_70000(benchmark, random_list):
    benchmark(create_heap, random_list[:70000])

def test_benchmark_create_4_ary_heap_80000(benchmark, random_list):
    benchmark(create_heap, random_list[:80000])

def test_benchmark_create_4_ary_heap_90000(benchmark, random_list):
    benchmark(create_heap, random_list[:90000])

def test_benchmark_create_4_ary_heap_100000(benchmark, random_list):
    benchmark(create_heap, random_list[:100000])

def test_benchmark_pop_4_ary_heap_10000(benchmark, random_list):
    heap = Heap(4, random_list)
    benchmark.pedantic(pop_top, args=(heap, 10000))

def test_benchmark_pop_4_ary_heap_20000(benchmark, random_list):
    heap = Heap(4, random_list)
    benchmark.pedantic(pop_top, args=(heap, 20000))

def test_benchmark_pop_4_ary_heap_30000(benchmark, random_list):
    heap = Heap(4, random_list)
    benchmark.pedantic(pop_top, args=(heap, 30000))

def test_benchmark_pop_4_ary_heap_40000(benchmark, random_list):
    heap = Heap(4, random_list)
    benchmark.pedantic(pop_top, args=(heap, 40000))

def test_benchmark_pop_4_ary_heap_50000(benchmark, random_list):
    heap = Heap(4, random_list)
    benchmark.pedantic(pop_top, args=(heap, 50000))

def test_benchmark_pop_4_ary_heap_60000(benchmark, random_list):
    heap = Heap(4, random_list)
    benchmark.pedantic(pop_top, args=(heap, 60000))

def test_benchmark_pop_4_ary_heap_70000(benchmark, random_list):
    heap = Heap(4, random_list)
    benchmark.pedantic(pop_top, args=(heap, 70000))

def test_benchmark_pop_4_ary_heap_80000(benchmark, random_list):
    heap = Heap(4, random_list)
    benchmark.pedantic(pop_top, args=(heap, 80000))

def test_benchmark_pop_4_ary_heap_90000(benchmark, random_list):
    heap = Heap(4, random_list)
    benchmark.pedantic(pop_top, args=(heap, 90000))

def test_benchmark_pop_4_ary_heap_100000(benchmark, random_list):
    heap = Heap(4, random_list)
    benchmark.pedantic(pop_top, args=(heap, 100000))