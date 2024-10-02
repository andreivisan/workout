#!/usr/bin/env python3

def switch(array: list[int], index: int, sorted_index: int):
    temp = array[index]
    array[index] = array[sorted_index]
    array[sorted_index] = temp

def insertion_sort(array: list[int]) -> list[int]:
    index = 1
    while index < len(array):
        sorted_index =  index - 1
        sorted_val = array[sorted_index]
        while sorted_index >= 0 and array[index] < sorted_val:
            switch(array, index, sorted_index)
            sorted_index -= 1
        index += 1
    return array

if __name__ == "__main__":
    array = [8, 4, 2, 9, 5]
    print(insertion_sort(array))

        
