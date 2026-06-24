import time
import random
import sys
from typing import List, Callable, Dict, Tuple

def bubble_sort(arr: List[int]) -> List[int]:
    """Bubble Sort Algorithm - O(n²)"""
    n = len(arr)
    arr_copy = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    return arr_copy

def insertion_sort(arr: List[int]) -> List[int]:
    """Insertion Sort Algorithm - O(n²)"""
    arr_copy = arr.copy()
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and arr_copy[j] > key:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    return arr_copy

def selection_sort(arr: List[int]) -> List[int]:
    """Selection Sort Algorithm - O(n²)"""
    arr_copy = arr.copy()
    n = len(arr_copy)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
    return arr_copy

def merge_sort(arr: List[int]) -> List[int]:
    """Merge Sort Algorithm - O(n log n)"""
    arr_copy = arr.copy()
    
    def merge(left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def sort(sub_arr: List[int]) -> List[int]:
        if len(sub_arr) <= 1:
            return sub_arr
        mid = len(sub_arr) // 2
        left = sort(sub_arr[:mid])
        right = sort(sub_arr[mid:])
        return merge(left, right)
    
    return sort(arr_copy)

def quick_sort(arr: List[int]) -> List[int]:
    """Quick Sort Algorithm - O(n log n) average case"""
    arr_copy = arr.copy()
    
    def partition(low: int, high: int) -> int:
        pivot = arr_copy[high]
        i = low - 1
        for j in range(low, high):
            if arr_copy[j] <= pivot:
                i += 1
                arr_copy[i], arr_copy[j] = arr_copy[j], arr_copy[i]
        arr_copy[i + 1], arr_copy[high] = arr_copy[high], arr_copy[i + 1]
        return i + 1
    
    def sort(low: int, high: int):
        if low < high:
            pi = partition(low, high)
            sort(low, pi - 1)
            sort(pi + 1, high)
    
    sort(0, len(arr_copy) - 1)
    return arr_copy

def run_sorting_experiment() -> Dict[str, List[float]]:
    """
    Orchestrator function to run all sorting algorithms for all input sizes
    Returns dictionary with timing results
    """
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }
    
    input_sizes = [100, 500, 1000, 5000]
    results = {algo_name: [] for algo_name in algorithms.keys()}
    
    print("=" * 70)
    print("SORTING ALGORITHMS PERFORMANCE EXPERIMENT")
    print("=" * 70)
    print(f"System: {sys.platform}")
    print(f"Python: {sys.version}")
    print("-" * 70)
    
    for size in input_sizes:
        print(f"\nTesting with input size: {size}")
        print("-" * 40)
        
        # Generate random array for current size
        random.seed(42)  # Fixed seed for reproducibility
        test_array = [random.randint(0, 10000) for _ in range(size)]
        
        for algo_name, algo_func in algorithms.items():
            # Create fresh copy for each algorithm
            arr_copy = test_array.copy()
            
            # Time the algorithm
            start_time = time.perf_counter()
            sorted_arr = algo_func(arr_copy)
            end_time = time.perf_counter()
            
            # Verify sorting is correct
            assert sorted_arr == sorted(test_array), f"{algo_name} failed to sort correctly!"
            
            # Record time in seconds
            elapsed = end_time - start_time
            results[algo_name].append(elapsed)
            
            print(f"{algo_name:20} | Time: {elapsed:.6f} seconds")
    
    return results

def display_results_table(results: Dict[str, List[float]]):
    """Display results in formatted table"""
    input_sizes = [100, 500, 1000, 5000]
    
    print("\n" + "=" * 90)
    print("OBSERVATION TABLE - Execution Times (seconds)")
    print("=" * 90)
    print(f"{'S/N':^5} | {'Input Size':^12} | {'Bubble Sort':^12} | {'Insertion Sort':^12} | "
          f"{'Selection Sort':^12} | {'Merge Sort':^12} | {'Quick Sort':^12}")
    print("-" * 90)
    
    for i, size in enumerate(input_sizes):
        print(f"{i+1:^5} | {size:^12} | "
              f"{results['Bubble Sort'][i]:^12.4f} | "
              f"{results['Insertion Sort'][i]:^12.4f} | "
              f"{results['Selection Sort'][i]:^12.4f} | "
              f"{results['Merge Sort'][i]:^12.4f} | "
              f"{results['Quick Sort'][i]:^12.4f}")
    
    print("=" * 90)

# Main execution
if __name__ == "__main__":
    print("Starting Sorting Algorithms Performance Analysis...")
    results = run_sorting_experiment()
    display_results_table(results)
    
    # Save results to file
    with open("sorting_results.txt", "w") as f:
        f.write("Sorting Algorithms Performance Results\n")
        f.write("=" * 60 + "\n")
        for algo, times in results.items():
            f.write(f"{algo}: {times}\n")
    
    print("\nResults saved to 'sorting_results.txt'")