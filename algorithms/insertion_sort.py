#!/usr/bin/env python3

def switch(array: list[int], index: int, sorted_index: int):
    temp = array[index]
    array[index] = array[sorted_index]
    array[sorted_index] = temp

def insertion_sort(array: list[int]) -> list[int]:
    n = len(array)
    for i in range(n-1):
        prev_index = i
        key_index = i + 1
        value_2ct = array[prev_index]
        key = array[key_index]
        while key < value_2ct and key_index >= 0 and prev_index >= 0:
            switch(array, key_index, prev_index)
            key_index -= 1
            prev_index -=1
            value_2ct = array[prev_index]
            key = array[key_index]
    return array

def insert_sorted(array: list[int], val: int, start: int, end: int) -> list[int]:
    if start > end:
        array.insert(start, val)
        return array
    
    mid = start + (end - start) // 2
    
    if array[mid] == val:
        array.insert(mid, val)
        return array
    elif val > array[mid]:
        return insert_sorted(array, val, mid + 1, end)
    else:
        return insert_sorted(array, val, start, mid - 1)

if __name__ == "__main__":
    array = [8, 4, 2, 9, 5]
    print(insertion_sort(array))
    print(insert_sorted(array, 11, 0, len(array) - 1))

        
