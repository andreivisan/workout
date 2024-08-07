# Algorithms workouts

## Arrays 

### Dynamic Arrays

A dynamic array is a data structure that provides a way to store elements in a contiguous block of memory but can resize itself to accommodate new elements. This flexibility in size makes dynamic arrays more versatile than static arrays, which have a fixed size.

#### Key Characteristics

1. Contiguous Memory: Elements are stored in contiguous memory locations, allowing for efficient access by index.

2. Dynamic Resizing: The array can grow or shrink as needed, though resizing usually involves some overhead.

#### How Dynamic Arrays Work

1. Initial Size and Capacity:

* A dynamic array starts with a certain initial capacity. The capacity is the total number of elements the array can hold before needing to resize.

2. Adding Elements:

* As elements are added, they are placed in the available slots of the array.

* When the array reaches its capacity, it resizes itself to accommodate more elements.

3. Resizing:

* When the current array is full and a new element needs to be added, the array allocates a new block of memory, typically double the size of the current capacity.

* All existing elements are copied to the new memory block, and the old memory block is freed.

4. Efficiency:

* Access: O(1) time complexity for accessing elements by index.

* O(1) average time complexity for adding elements, although individual additions may sometimes require O(n) time due to resizing.

* Resizing Cost: The amortized cost of resizing is spread out over many insertions, making the average time per insertion O(1).

[Dynamic Array](dynamic_array.py)

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

### Two Pointers

#### Concept:

* Two pointers is a technique used to iterate through an array or list with two variables pointing to different indices.

* Common use cases include problems involving pairs, triplets, or partitions within an array.

#### Applications:

* Sorted Arrays: Finding pairs that sum to a specific target.

* Linked Lists: Detecting cycles, finding the middle element.

* String Manipulation: Palindrome checking, string reversal.

[Two Pointers - Two Sum 2](two_sum_2.py)

### Sliding Window

#### Concept:

* The sliding window technique involves maintaining a window that slides over the data structure to optimize the solution's performance.

* It is particularly useful for problems involving subarrays, substrings, or sequences.

#### Types of Sliding Windows:

1. Fixed-Size Window: The window size remains constant.

2. Dynamic-Size Window: The window size can change based on conditions.

#### Applications:

* Subarray Problems: Maximum sum subarray, smallest subarray with a given sum.

* Substring Problems: Longest substring without repeating characters.


## Stacks

A stack is a fundamental data structure in computer science that operates on a Last In, First Out (LIFO) principle. This means that the last element added to the stack will be the first one to be removed. Let's explore stacks from both a software perspective and a deeper, hardware-level understanding.

### Basic Operations

1. Push: Adds an element to the top of the stack.

2. Pop: Removes and returns the top element from the stack.

3. Peek (or Top): Returns the top element without removing it.

4. isEmpty: Checks if the stack is empty.

### Summary

* Software Level: Stacks are used for function call management, expression evaluation, and more. They can be implemented using arrays or linked lists.

* Hardware Level: Stacks are managed using a stack pointer and are critical for managing control flow and function calls. The stack is implemented in RAM and operates on binary data at the hardware level.

### How Stacks work in memory

Example for a function call to add 2 numbers:

1. Parameters and return address are pushed onto the stack by the caller.

2. The callee function saves the current frame pointer and sets up a new frame pointer.

3. The function body accesses parameters and local variables relative to the frame pointer.

4. Upon completion, the function cleans up the stack and restores the previous frame pointer and return address.

5. Control is transferred back to the caller using the return address.

[How Stacks Work in Memory](stack_visualisation.py)

[LeetCode Valid Parentheses Problem](valid_parentheses.py)


## Singly Linked Lists

A singly linked list is a data structure that consists of a sequence of elements called nodes. Each node contains two components:

1. Data: The value stored in the node.

2. Next: A reference (or pointer) to the next node in the sequence.

In a singly linked list, each node points to the next node in the list, forming a chain of nodes. The list starts with a head node, and the end of the list is marked by a node that points to None (null reference), indicating there are no further nodes.

### Key Operations

1. Insertion: Adding a new node to the list.

2. Deletion: Removing a node from the list.

3. Traversal: Accessing each node's data in the list.

4. Search: Finding a node with a specific value.

### Key Points

1. Node: The basic unit of a linked list, containing data and a pointer to the next node.

2. Head: The first node in the list.

3. Traversal: Start from the head and follow the next pointers to visit each node.

4. Insertion: Can be done at the beginning (prepend), end (append), or between nodes.

5. Deletion: Involves updating the next pointer of the previous node to skip the deleted node.

### Advantages and Disadvantages

#### Advantages:

* Dynamic Size: Can easily grow and shrink as elements are added or removed.

* Efficient Insertions/Deletions: No need to shift elements as in arrays.

#### Disadvantages:

* Memory Overhead: Requires extra memory for storing pointers.

* Sequential Access: Requires traversal from the head to access elements, making it slower than random access in arrays.

Singly linked lists are foundational data structures used in various applications, including stacks, queues, and graph representations.

[Singly Linked List implementation](singly_linked_list.py)

[Reverse Singly Linked List](reverse_linked_list.py)

[Merge Two Sorted Linked Lists](merge_2_sorted_lists.py)


## Doubly Linked Lists

A doubly-linked list is a type of linked list in which each node contains three components:

1. Data: The value stored in the node.

2. Next: A reference (or pointer) to the next node in the sequence.

3. Prev: A reference (or pointer) to the previous node in the sequence.

### Key Operations

1. Insertion: Adding a new node to the list.

2. Deletion: Removing a node from the list.

3. Traversal: Accessing each node's data in the list.

4. Search: Finding a node with a specific value.

### Implementation in Python

[Doubly Linked List](doubly_linked_list.py)


## Sorting

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


## Recursion

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


## Hashing

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



