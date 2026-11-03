"""Practical 5: Deterministic and randomized Quick Sort."""
import random


def partition(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def quick_sort(a, low, high, randomized=False):
    if low < high:
        if randomized:
            pivot_index = random.randint(low, high)
            a[pivot_index], a[high] = a[high], a[pivot_index]
        p = partition(a, low, high)
        quick_sort(a, low, p - 1, randomized)
        quick_sort(a, p + 1, high, randomized)


def main():
    values = list(map(int, input("Enter numbers separated by spaces: ").split()))
    deterministic = values.copy()
    randomized = values.copy()
    quick_sort(deterministic, 0, len(deterministic) - 1)
    quick_sort(randomized, 0, len(randomized) - 1, randomized=True)
    print("Deterministic Quick Sort:", deterministic)
    print("Randomized Quick Sort:   ", randomized)
    print("Best/average: O(n log n); worst: O(n^2). Randomization reduces the risk of consistently poor pivots.")

if __name__ == '__main__':
    main()
