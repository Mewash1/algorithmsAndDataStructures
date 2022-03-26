import json
from matplotlib import pyplot as plt


class Sortings:
   'Helps with detaling results'

   def __init__(self) -> None:
      self._sortings = ['bubble', 'selection', 'merge', 'quick']

   def added_sorting(self, name):
      for sorting in self._sortings:
         if sorting in name:
            self._sortings.remove(sorting)
            return sorting + '_sort'
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
   'Details results from the base json sturct'
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


def plot_reuslts(results: dict):
   'Plots statistics'
   amount = [1000, 2000, 5000, 7000, 10000]
   ticks = [1000, 2000, 3000, 4000, 5000, 6000,
   7000, 8000, 9000, 10000]
   for name, values in results.items():
      plt.plot(values, amount, 'o-')
      plt.yticks(ticks)
      plt.title(name)
      plt.xlabel('nanoseconds')
      plt.ylabel('number of words')
      plt.savefig(f'stats/{name}.png', format='png')
      plt.clf()

   for name, values in results.items():
      plt.plot(values, amount, 'o-', label=name)
      plt.yticks(ticks)
      plt.title('Sortings compared')
      plt.xlabel('nanoseconds')
      plt.ylabel('number of words')
      plt.legend()
      plt.savefig(f'stats/sortings_compared.png', format='png')



def main():
   reuslts = open_results()
   plot_reuslts(reuslts)

if __name__ == "__main__":
   main()