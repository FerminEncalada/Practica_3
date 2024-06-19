import sys
sys.path.append('../')  # Ajusta la ruta según la ubicación de tu archivo sorting.py

import random
import time
from controls.tda.linked.merge import MergeSort
from controls.tda.linked.quick import QuickSort
from controls.tda.linked.shell import ShellSort
from controls.tda.linked.binarySearch import BinarySearch
from controls.tda.linked.linearSearch import LinearSearch 
from controls.personaDaoControl import PersonaDaoControl
from controls.tda.linked.linkedList import Linked_List
from tabulate import tabulate

pcd = PersonaDaoControl()

def main():
    sizes = [10000, 20000, 25000]
    sorters = {
        "MergeSort": MergeSort(),
        "QuickSort": QuickSort(),
        "ShellSort": ShellSort()
    }
    searchers = {
        "BinarySearch": BinarySearch(),
        "LinearSearch": LinearSearch()
    }

    timing_results = {"sorting": {}, "searching": {}}
   
    for size in sizes:
        print(f"\nTamaño de array: {size}")
       
        # Medición de tiempo para algoritmos de ordenamiento
        timing_results["sorting"][size] = {}
        data = [random.randint(1, 100000) for _ in range(size)]
       
        for sorter_name, sorter in sorters.items():
            data_copy = data.copy()
            start_time = time.time()
            sorter.sort_primitive_ascendent(data_copy)
            end_time = time.time()
            timing_results["sorting"][size][sorter_name] = end_time - start_time
       
        # Medición de tiempo para algoritmos de búsqueda
        timing_results["searching"][size] = {}
        query = random.choice(data)
        query_attribute = 0  # Usado para búsqueda en datos primitivos

        for searcher_name, searcher in searchers.items():
            data_copy = data.copy()
            start_time = time.time()
            searcher.search(data_copy, query_attribute, query, starts_with=False)
            end_time = time.time()
            timing_results["searching"][size][searcher_name] = end_time - start_time

    # Imprimir resultados
    for size, results in timing_results["sorting"].items():
        print(f"\nResultados de ordenamiento para tamaño {size}:")
        table = [[sorter_name, time_taken] for sorter_name, time_taken in results.items()]
        print(tabulate(table, headers=["Algoritmo de Ordenamiento", "Tiempo (segundos)"], tablefmt="pretty"))

    for size, results in timing_results["searching"].items():
        print(f"\nResultados de búsqueda para tamaño {size}:")
        table = [[searcher_name, time_taken] for searcher_name, time_taken in results.items()]
        print(tabulate(table, headers=["Algoritmo de Búsqueda", "Tiempo (segundos)"], tablefmt="pretty"))

if __name__ == "__main__":
    main()
