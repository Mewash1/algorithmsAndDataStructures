import json
from matplotlib import pyplot as plt
import os


class Sortings:
    '''Helps with detaling results'''

    def __init__(self) -> None:
        self._sortings = ["create", "pop"]

    def added_sorting(self, name):
        for sorting in self._sortings:
            if sorting in name:
                self._sortings.remove(sorting)
                return sorting + '_heap'
        return None


def open_results():
    with open("results.json", 'r') as handle:
        reuslts = read_results(handle)
    return reuslts


def read_results(handle) -> dict:
    whole_results = json.load(handle)
    results = detail_results(whole_results)
    return results


def detail_results(whole_results: dict) -> dict:
    '''Details results from the base json sturct'''
    results = {}
    sortings = Sortings()
    for benchmark in whole_results['benchmarks']:
        name = benchmark['name']
        sorting = sortings.added_sorting(name)
        if sorting is not None:
            sorting_name = sorting
            results[sorting_name] = []
        mean = benchmark['stats']['mean']
        results[sorting_name].append(mean)
    return results


def creating_dir_for_stats():
    name = 'statistics'
    if not os.path.exists(name):
        os.mkdir(name)


def plot_reuslts(results: dict):
    '''Plots statistics'''
    creating_dir_for_stats()
    amount = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
    ticks = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
    for name, values in results.items():
        plt.plot(amount, values[:10], 'o-', label="2-ary")
        plt.plot(amount, values[10:20], 'o-', label="3-ary")
        plt.plot(amount, values[20:], 'o-', label="4-ary")
        plt.legend()
        plt.xticks(ticks)
        plt.title(name)
        plt.ylabel('miliseconds')
        plt.xlabel('number of elements')
        plt.savefig(f'statistics/{name}.png', format='png')
        #plt.clf()
        plt.show()

def main():
    reuslts = open_results()
    plot_reuslts(reuslts)


if __name__ == "__main__":
    main()
