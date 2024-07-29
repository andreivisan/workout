# Algorithms workouts

## Day 1

### Binary Search

#### Steps of Binary Search

1. Initialize: Start with two pointers, one at the beginning (low) and one at the end (high) of the array.

2. Middle Point: Calculate the middle point of the current interval.

3. Comparison:

    * If the middle element is equal to the target value, the search is complete.

    * If the target value is less than the middle element, adjust the high pointer to mid - 1.

    * If the target value is greater than the middle element, adjust the low pointer to mid + 1.

4. Repeat: Repeat steps 2 and 3 until the low pointer is greater than the high pointer.
