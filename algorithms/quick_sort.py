#!/usr/bin/env python3

def quick_sort(array: list[int], low: int, high: int):
    if low < high:
        pivot_index = partition_pivot_first(array, low, high)
        quick_sort(array, low, pivot_index - 1)
        quick_sort(array, pivot_index + 1, high)

def partition_pivot_first(array: list[int], low: int, high: int) -> int:
    pass

def swap(array: list[int], i: int, j: int):
    array[i], array[j] = array[j], array[i]

if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    quick_sort(array, 0, len(array))
    print(array)