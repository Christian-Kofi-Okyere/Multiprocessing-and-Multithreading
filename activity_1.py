"""Activity 1"""

import time
from multiprocessing import Pool, cpu_count

def sum_of_squares(n):
    return sum([i * i for i in range(n)])

def main():
    N = 10**7  # Large number for heavy computation
    num_tasks = 4  # Number of parallel tasks

    start_time = time.time()  # Start time for performance measurement

    with Pool(processes=min(cpu_count(), num_tasks)) as pool:
        results = pool.map(sum_of_squares, [N] * num_tasks)

    end_time = time.time()  # End time for performance measurement
    print("Parallel Execution Time (multiprocessing):", end_time - start_time)


if __name__ == "__main__":
    main()



