import json
import time
from heapsort.heapsort import heapsort
from quicksort.quicksort import iterative_quicksort
from insertionsort.insertionsort import insertion_sort

def load_data():
    with open('sorting\data.json', 'r') as file:
        return json.load(file)
def time_sort(entry):
    t = time.process_time()
    entry['sorting_algo'](entry['arr'])
    elapsed_time = time.process_time()-t
    print(f"It took us {elapsed_time} to perform {entry['name']} on {entry['num_items']}")
def main():
    data = load_data()
    algos = [(heapsort,'heapsort'),(iterative_quicksort,'quicksort'),(insertion_sort,'insertionsort')]
    for k,v in data.items():
        for algo in algos:
            time_sort({
                'sorting_algo': algo[0],
                'arr': v,
                'name': algo[1],
                'num_items':k
            })
if __name__ =="__main__":
    main()