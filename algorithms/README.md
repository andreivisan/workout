# Algorithms workouts

## Day 1

### Binary Search

#### Steps of Binary Search

1. Initialize: Start with two pointers, one at the beginning (low) and one at the end (high) of the array.

2. Middle Point: Calculate the middle point of the current interval. ``` mid = low + (high - low) // 2 ```

3. Comparison:

    * If the middle element is equal to the target value, the search is complete.

    * If the target value is less than the middle element, adjust the high pointer to mid - 1.

    * If the target value is greater than the middle element, adjust the low pointer to mid + 1.

4. Repeat: Repeat steps 2 and 3 until the low pointer is greater than the high pointer.


### Bubble Sort

#### Steps of Bubble Sort

1. Start at the beginning of the list.

2. Compare the first two elements:

    * If the first element is greater than the second element, swap them.

3. Move to the next pair of elements, compare them, and swap if necessary.

4. Continue this process for each pair of adjacent elements to the end of the list. This completes one pass.

5. Repeat the process for the entire list for (n-1) passes (where n is the number of elements in the list). With each pass, the largest element "bubbles up" to its correct position, reducing the number of elements to be compared in subsequent passes.

6. End the process when no swaps are needed in a pass, indicating that the list is sorted.
