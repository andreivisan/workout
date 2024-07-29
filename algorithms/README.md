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


### Recursion

#### Intro

Recursion is a programming technique where a function calls itself directly or indirectly to solve a problem. 
A recursive function typically has two main components:

    * Base Case: The condition under which the function stops calling itself. Without a base case, the function would call itself indefinitely, leading to a stack overflow.
    
    * Recursive Case: The part of the function where it calls itself with modified parameters, gradually reducing the problem size.

#### Steps for Understanding Recursion

1. Identify the Base Case: Determine the simplest instance of the problem, which can be solved directly.

2. Identify the Recursive Case: Break down the larger problem into smaller instances of the same problem.

3. Combine Results: Ensure that each recursive call progresses towards the base case and combines results correctly.

#### Memoization

##### How Memoization Works

1. Function Call: When a function is called, check if the result for the given input is already stored (cached).

2. Return Cached Result: If the result is found in the cache, return it immediately, avoiding redundant computations.

3. Compute and Cache Result: If the result is not in the cache, compute it and store the result in the cache before returning it.

##### Steps for Implementing Memoization

1. Create a Cache: Use a data structure (like a dictionary in Python) to store the results of function calls.

2. Check Cache Before Computing: Before performing the computation, check if the result is already in the cache.

3. Store the Result in Cache: After computing the result, store it in the cache with the corresponding input as the key.
