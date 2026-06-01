import random
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_list(arr):
    print(" ".join(str(x) for x in arr))

def bubble_sort_visual(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            clear()
            print("Sorting...")
            print_list(arr)

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            time.sleep(0.1)

    clear()
    print("Sorted!")
    print_list(arr)

# generate random list
data = [random.randint(1, 20) for _ in range(10)]

bubble_sort_visual(data)
