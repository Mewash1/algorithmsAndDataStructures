import random, pytest
from ..d_ary_heap import Heap

@pytest.fixture
def random_list():
    random_list = []
    for _ in range(100000):
        random_list.append(random.randint(1, 30000))
    return random_list

def test_benchmark_create_2_ary_heap_10000(benchmark, random_list):
    heap = Heap(2)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:10000]))

def test_benchmark_create_2_ary_heap_20000(benchmark, random_list):
    heap = Heap(2)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:20000]))

def test_benchmark_create_2_ary_heap_30000(benchmark, random_list):
    heap = Heap(2)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:30000]))

def test_benchmark_create_2_ary_heap_40000(benchmark, random_list):
    heap = Heap(2)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:40000]))

def test_benchmark_create_2_ary_heap_50000(benchmark, random_list):
    heap = Heap(2)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:50000]))

def test_benchmark_create_2_ary_heap_60000(benchmark, random_list):
    heap = Heap(2)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:60000]))

def test_benchmark_create_2_ary_heap_70000(benchmark, random_list):
    heap = Heap(2)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:70000]))

def test_benchmark_create_2_ary_heap_80000(benchmark, random_list):
    heap = Heap(2)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:80000]))

def test_benchmark_create_2_ary_heap_90000(benchmark, random_list):
    heap = Heap(2)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:90000]))

def test_benchmark_create_2_ary_heap_100000(benchmark, random_list):
    heap = Heap(2)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:100000]))


def test_benchmark_create_3_ary_heap_10000(benchmark, random_list):
    heap = Heap(3)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:10000]))

def test_benchmark_create_3_ary_heap_20000(benchmark, random_list):
    heap = Heap(3)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:20000]))

def test_benchmark_create_3_ary_heap_30000(benchmark, random_list):
    heap = Heap(3)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:30000]))

def test_benchmark_create_3_ary_heap_40000(benchmark, random_list):
    heap = Heap(3)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:40000]))

def test_benchmark_create_3_ary_heap_50000(benchmark, random_list):
    heap = Heap(3)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:50000]))

def test_benchmark_create_3_ary_heap_60000(benchmark, random_list):
    heap = Heap(3)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:60000]))

def test_benchmark_create_3_ary_heap_70000(benchmark, random_list):
    heap = Heap(3)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:70000]))

def test_benchmark_create_3_ary_heap_80000(benchmark, random_list):
    heap = Heap(3)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:80000]))

def test_benchmark_create_3_ary_heap_90000(benchmark, random_list):
    heap = Heap(3)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:90000]))

def test_benchmark_create_3_ary_heap_100000(benchmark, random_list):
    heap = Heap(3)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:100000]))


def test_benchmark_create_4_ary_heap_10000(benchmark, random_list):
    heap = Heap(4)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:10000]))

def test_benchmark_create_4_ary_heap_20000(benchmark, random_list):
    heap = Heap(4)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:20000]))

def test_benchmark_create_4_ary_heap_30000(benchmark, random_list):
    heap = Heap(4)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:30000]))

def test_benchmark_create_4_ary_heap_40000(benchmark, random_list):
    heap = Heap(4)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:40000]))

def test_benchmark_create_4_ary_heap_50000(benchmark, random_list):
    heap = Heap(4)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:50000]))

def test_benchmark_create_4_ary_heap_60000(benchmark, random_list):
    heap = Heap(4)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:60000]))

def test_benchmark_create_4_ary_heap_70000(benchmark, random_list):
    heap = Heap(4)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:70000]))

def test_benchmark_create_4_ary_heap_80000(benchmark, random_list):
    heap = Heap(4)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:80000]))

def test_benchmark_create_4_ary_heap_90000(benchmark, random_list):
    heap = Heap(4)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:90000]))

def test_benchmark_create_4_ary_heap_100000(benchmark, random_list):
    heap = Heap(4)
    benchmark.pedantic(heap.__init__, args=(2, random_list[:100000]))
