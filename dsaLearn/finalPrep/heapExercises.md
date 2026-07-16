# Heap Practice Exercises

Practice set for quiz / final prep. Focus: **Insertion**, **Deletion**, **Heapify**, **Make Heap**, and **Heap Sort**.

Work on paper first. Then implement the programming section without using Python’s `heapq` for the core logic.

---

## Objectives

- Trace max-heap and min-heap operations by hand
- Convert between tree drawings and array form
- Perform bottom-up `make_heap` with `heapify`
- Trace heapsort until the array is sorted
- Implement a list-backed heap in Python

---

## Quick formulas (0-based)

```text
parent(i) = (i - 1) // 2
left(i)   = 2 * i + 1
right(i)  = 2 * i + 2
last non-leaf = n // 2 - 1
```

---

## Part A — Paper / In Class Style

### A1. Heap Insertion (Max-Heap)

Start with an **empty max-heap**. Insert the values below one by one.

**Values:** `12, 7, 15, 3, 9, 20, 8, 1, 18, 5`

For each insertion:

1. Append the value as the next leaf (keep completeness)
2. Sift / percolate **up** until heap-order is restored
3. Draw the heap **after each insertion**
4. Also write the **array form** after each insertion

**Checkpoint:** After all inserts, verify every parent ≥ its children.

---

### A2. Heap Insertion (Min-Heap)

Start with an **empty min-heap**. Insert:

**Values:** `10, 6, 5, 4, 9, 16, 7, 18, 22, 1, 3, 8, 2, 11`

Same rules as A1, but parent must stay **≤** children (sift up when child is smaller).

Draw the heap after each insertion.

---

### A3. Heap Removal / Delete-Max

You are given this **max-heap** in array form:

```text
[60, 30, 36, 20, 22, 27, 15, 14, 17, 21, 5, 24, 26, 6, 12]
```

1. Draw the complete binary tree
2. Perform **delete-max** (remove root) **4 times**
3. After each removal:
   - Swap root with last leaf
   - Remove the last leaf (the old max)
   - Sift / percolate **down** the new root
   - Redraw the heap
   - Write the new array

**Optional stretch:** continue until the heap is empty.

---

### A4. Heap Removal / Delete-Min

You are given this **min-heap** in array form:

```text
[1, 3, 2, 8, 5, 6, 4, 12, 10, 9, 7, 15]
```

1. Draw the heap
2. Perform **delete-min** **3 times**
3. Redraw and write the array after each removal

---

### A5. Make Heap (Bottom-up Heapify)

You are given this unsorted array:

```text
[11, 2, 5, 6, 7, 8, 9, 12, 4, 10, 1, 3, 15, 13, 14]
```

1. Draw the complete binary tree represented by the array
2. Find the **last non-leaf** index: `n // 2 - 1`
3. Starting from that index and moving **left toward the root**, call **heapify** (sift-down) on each index until you have a **max-heap**
4. Redraw the heap after **each** heapify call
5. Write the final array form of the max-heap

**Explain (short):** Why do we start from the last non-leaf instead of the root?

---

### A6. Heapify Spot Check

For each array, answer:

- Is it already a max-heap? Yes / No
- If No, which index first violates heap-order?
- Perform **one** `heapify` at that index (or at the parent of the violation) and show the result

1. `[90, 70, 80, 50, 60, 75]`
2. `[90, 80, 70, 85, 60]`
3. `[40, 30, 35, 10, 20, 50]`
4. `[5, 4, 3, 2, 1]`

---

### A7. Heap Sort

Start from the **max-heap** you built in **A5**.

1. Write the array form of that max-heap
2. Repeat until sorted ascending:
   1. Swap root with the last heap element
   2. Shrink the heap size by 1 (sorted zone grows from the right)
   3. Heapify / percolate down at index `0` on the remaining heap only
3. After each number is moved into the sorted zone, write the full array and mark which part is sorted
4. Stop when the array is sorted in **ascending** order

**Shorter alternate start** (if A5 took too long):

```text
Max-heap start: [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
```

---

### A8. Mixed Tracing Quiz

Answer without code first.

1. Insert `45` into max-heap `[50, 30, 40, 10, 20, 35]`. Final array?
2. One `delete_max` on your result from (1). Final array?
3. For array `[10, 20, 15, 30, 40]`, show `make_heap` into a max-heap (heapify from last non-leaf).
4. Why must a heap be a **complete** binary tree?
5. Time complexity of:
   - insert
   - delete-max
   - heapify (one call)
   - make_heap (bottom-up)
   - heapsort

---

## Part B — Programming

Implement a **MaxHeap** class using an array / Python list (as discussed in class).

When `MaxHeap` is created:

- If a list is provided, copy it and run `make_heap()` to build a max-heap in place on that copy
- If no list is provided, start empty

Do **not** use `heapq` for these methods.

---

```python
def is_empty(self):
```

Returns `True` if the heap has no items, otherwise `False`.

---

```python
def size(self):
```

Returns the number of items stored in the heap.

---

```python
def peek(self):
```

Returns the maximum item without removing it.  
Returns `None` if the heap is empty.

---

```python
def push(self, data):
```

Inserts `data` into the max-heap (append + sift-up).

---

```python
def pop(self):
```

Removes and returns the maximum item.  
Returns `None` if the heap is empty.

---

```python
def heapify(self, i, n=None):
```

Sifts down the node at index `i`.  
`n` is the current heap size (important for heapsort / partial heaps).

---

```python
def make_heap(self):
```

Turns the internal list into a max-heap using bottom-up heapify.

---

### Optional B2 — MinHeap

Repeat Part B for a **MinHeap**:

- `push` / `pop` / `peek` use min-heap order
- Constructor may accept a list and call `make_heap()` for a min-heap

---

### Optional B3 — Heapsort Function

```python
def heapsort(values: list) -> list:
```

Returns a **new** list sorted ascending, using a max-heap approach:

1. Build a max-heap
2. Repeatedly move max to the end and heapify the shrinked prefix

Do not call Python’s built-in `sorted()` / `.sort()` inside this function.

---

## Part C — Test Cases (run your code)

| Case | Action | Expected idea |
|---|---|---|
| Empty | `pop()` / `peek()` on empty heap | returns `None` |
| One item | push `7`, then pop | pop returns `7`, heap empty |
| Duplicates | push `5, 5, 5` | still valid heap; pops return `5` |
| Build from list | `MaxHeap([1, 2, 3, 4, 5])` | internal array is a max-heap |
| Alternating ops | push / pop mixed | after each op, parent ≥ children |
| Only left child | heap size 2 or 4 | sift-down handles missing right child |
| Heapsort | `heapsort([5, 1, 4, 2])` | `[1, 2, 4, 5]` |

---

## Self-Check Rubric

| Criteria | Not yet | Getting there | Ready |
|---|---|---|---|
| Insertion | Cannot sift-up correctly | Trace mostly works, misses a swap | Correct tree + array after every insert |
| Deletion | Loses completeness or order | One removal works | Multiple removals correct |
| Heapify / Make Heap | Starts at wrong index | Fixes some nodes | Full bottom-up build correct |
| Heap Sort | Confuses sorted zone | Almost sorted | Fully ascending with correct traces |
| Coding | Methods incomplete | Works on happy path | Handles empty / duplicates / build-from-list |

---

## Suggested order

1. A1 or A2 (insertion warm-up)
2. A3 (deletion)
3. A5 → A7 (make heap then heapsort)
4. A8 (quick quiz)
5. Part B + Part C (implementation)
