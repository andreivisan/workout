#!/usr/bin/env python3

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high: 
        mid = low + (high - low) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return - 1

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    print(binary_search(nums, target))
 
