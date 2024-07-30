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

[Binary Search](binary_search.py)


### Bubble Sort

#### Steps of Bubble Sort

1. Start at the beginning of the list.

2. Compare the first two elements:

    * If the first element is greater than the second element, swap them.

3. Move to the next pair of elements, compare them, and swap if necessary.

4. Continue this process for each pair of adjacent elements to the end of the list. This completes one pass.

5. Repeat the process for the entire list for (n-1) passes (where n is the number of elements in the list). With each pass, the largest element "bubbles up" to its correct position, reducing the number of elements to be compared in subsequent passes.

6. End the process when no swaps are needed in a pass, indicating that the list is sorted.

[Bubble Sort](bubble_sort.py)


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

[Fibonacci](recursion_fibonacci.py)


## Day 2

### Hashing

Hashing is a fundamental concept in computer science, used extensively for data storage and retrieval. At a lower level, hashing involves intricate memory management and data manipulation. Let's delve into what happens in memory when hashing is implemented.

#### Key Concepts in Hashing

<b>1. Hash Function:</b>

* A hash function is a mathematical function that converts an input (or 'key') into a fixed-size string of bytes, typically a hash code.

* The output (hash code) is usually used as an index to place or locate data in a hash table.

<b>2. Hash Table:</b>

* A hash table is a data structure that stores key-value pairs. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

#### Memory Operations in Hashing

<b>1. Memory Allocation:</b>

* When a hash table is initialized, a block of memory is allocated for the array of buckets. The size of this array (often a power of two) determines the range of possible indices.

<b>2. Hash Code Calculation: </b>

* When a key is inserted, the hash function is applied to the key, resulting in a hash code. This hash code is then used to calculate an index in the array of buckets.

<b>3. Handling Collisions:</b>

* Direct Addressing: The hash code itself is used as an index if the number of possible keys is relatively small.

* Open Addressing: If a collision occurs (i.e., two keys hash to the same index), the algorithm searches for the next available slot.

* Chaining: Each bucket contains a linked list of all elements that hash to the same index. This involves dynamic memory allocation for list nodes as new elements are added.

<b>4. Insertion Process:</b>

* For chaining, the new key-value pair is appended to the linked list at the calculated index.

* For open addressing, if the calculated index is occupied, the algorithm probes to find an empty slot based on a defined probing sequence.

<b>5. Retrieval:</b>

* To retrieve a value, the hash function is applied to the key, and the resulting index is used to access the bucket.

* If using chaining, the linked list is traversed to find the matching key. If using open addressing, the probing sequence is followed until the key is found or an empty slot is reached.

<b>6. Deletion: </b>

* In chaining, the corresponding node in the linked list is removed.

* In open addressing, the deleted element might be marked with a special "deleted" marker to avoid disrupting the probing sequence for other elements.

#### Memory-Level Details

<b>1. Cache Efficiency:</b>

* Hash tables are designed to optimize cache utilization. When keys are spread uniformly across the table, it maximizes the likelihood that successive accesses will hit the cache, reducing access times.

<b>2. Memory Alignment:</b>

* Hash tables often align memory allocation to word boundaries to optimize access speeds. Modern CPUs handle memory in chunks (words), so aligning data structures accordingly can improve performance.

<b>3. Resizing:</b> 

* When the hash table becomes too full (a high load factor), it may resize itself, usually doubling in size. This involves allocating a new array and rehashing all existing elements into the new array, a process known as rehashing.

<b>4. Collision Resolution and Probing:</b>

* Linear Probing: Moves sequentially to the next slot.

* Quadratic Probing: Moves quadratically in the table.

* Double Hashing: Uses a second hash function to determine the step size.

#### Practical Considerations

<b>1. Load Factor:</b>

* The load factor, defined as n / k (where n is the number of elements and k is the number of buckets), influences performance. A high load factor increases the likelihood of collisions, degrading performance.

<b>2. Hash Function Quality:</b>

* A good hash function distributes keys uniformly across the hash table, minimizing collisions. Poor hash functions can lead to clustering, where many keys hash to the same index, increasing the average retrieval time.

<b>3. Security Concerns:</b>

Hash functions should be resistant to hash collisions to prevent attacks like hash flooding, where an adversary intentionally causes many collisions to degrade the performance of a hash table.
