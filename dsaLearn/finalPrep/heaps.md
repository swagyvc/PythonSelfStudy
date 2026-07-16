# Quiz Preparation — Heaps (Max-Heap Focus)

**Goal:** You already know Insert / Delete / Heapify / Sorting on paper. In 3 days (60–90 min each), bridge that to *why* it works and how to *implement* a list-backed max-heap in Python — no `heapq` for core practice.

**Validation target (you are ready when you can):**

- Derive index formulas from memory and use them correctly
- Implement insert, delete-max, heapify, make_heap, heapsort without looking up code
- Explain why bottom-up build is O(n) vs repeated insert O(n\log n)
- Trace heapsort on a small array and state every key time complexity

---



## Topic Checklist (from your notes)

Use this as a running checklist. Check items off as you finish each day.

- [ ] Definition of Heaps — what are they?
- [ ] Formula to find child and parent — why we need it, how to apply it
- [ ] Full Binary Tree vs Complete Binary Tree
- [ ] Insert / Delete from heaps
- [ ] How they are implemented — underlying data structure
- [ ] Heap order and completeness
- [ ] Heapify — what it is and why people use it
- [ ] How to perform `make_heap()` in place using `heapify()`
- [ ] Heapsort
- [ ] Time complexity: Create / Make Heap / Insert / Delete / Heapify / Sorting
- [ ] Trees: leaf, root, sibling, height, depth, complete, traversals, branches, etc.

---



## Quick Reference (keep open while coding)



### What is a heap?

A **heap** is a **complete binary tree** that also satisfies the **heap-order** property.


| Property         | Meaning (max-heap)                                |
| ---------------- | ------------------------------------------------- |
| **Completeness** | Filled level by level, left to right. No gaps.    |
| **Heap order**   | Every parent ≥ its children. Root is the maximum. |


**Student analogy:** Imagine students lining up for office hours by "urgency score." The student with the highest score must be at the front. The line does not need to be perfectly sorted after that, but every student must be at least as urgent as the students directly behind them in their small group. That is a max-heap: the top is guaranteed to be the maximum, but the entire structure is not fully sorted.

Example max-heap list:

```text
[90, 70, 80, 50, 60, 75]

        90
       /  \
     70    80
    / \   /
  50  60 75
```

This is valid because each parent is bigger than its own children: `90 >= 70,80`, `70 >= 50,60`, and `80 >= 75`.

**Underlying structure in code:** usually a **Python list / array** (not linked nodes). Completeness lets us store the tree in contiguous indices with no pointers.

### Full vs Complete Binary Tree


|                    | Full                           | Complete                                                                 |
| ------------------ | ------------------------------ | ------------------------------------------------------------------------ |
| Definition         | Every node has 0 or 2 children | All levels full except possibly the last; last level filled left → right |
| Required for heap? | No                             | **Yes**                                                                  |


A heap must be **complete**. It does not have to be full.

**Analogy:** A complete tree is like filling classroom seats from the front row to the back row, left to right. You are allowed to stop halfway through the last row, but you are not allowed to skip a seat and then fill a later one.

Valid complete shape:

```text
        A
       / \
      B   C
     / \
    D   E
```

Invalid for a heap shape because there is a gap before a later child:

```text
        A
       / \
      B   C
       \
        E
```

### Tree vocabulary (quiz-ready)


| Term               | Definition                                                                                      |
| ------------------ | ----------------------------------------------------------------------------------------------- |
| **Root**           | Top node (index 0 in the array)                                                                 |
| **Leaf**           | Node with no children                                                                           |
| **Sibling**        | Nodes that share the same parent                                                                |
| **Parent / Child** | Linked by heap-order and index formulas                                                         |
| **Depth**          | Edges from root to the node (root depth = 0)                                                    |
| **Height**         | Longest path down from a node to a leaf (leaf height = 0; tree height ≈ \lfloor\log_2 n\rfloor) |
| **Branch**         | Edge from parent to child                                                                       |
| **Traversals**     | Level-order ≈ walking the array left → right; pre/in/post-order less common for heap ops        |




### Index formulas (0-based Python lists)

For node at index `i`:

```text
parent(i) = (i - 1) // 2
left(i)   = 2 * i + 1
right(i)  = 2 * i + 2
```

**Why use formulas?** The array *is* the tree. Formulas replace left/right/parent pointers. Apply them whenever you walk up (insert / sift-up) or down (delete / heapify).

**Last non-leaf index** (start of bottom-up build): `n // 2 - 1`

**Seat-number analogy:** Think of the array as numbered seats in a theater filled row by row. If a student is sitting in seat `i`, the formulas instantly tell you where their parent seat and child seats are. No one needs to point at anyone else; the seat numbers encode the family relationship.

Example with `[90, 70, 80, 50, 60, 75]`:

| Index | Value | Parent index | Left child | Right child |
|---|---:|---:|---:|---:|
| 0 | 90 | none | 1 -> 70 | 2 -> 80 |
| 1 | 70 | 0 -> 90 | 3 -> 50 | 4 -> 60 |
| 2 | 80 | 0 -> 90 | 5 -> 75 | none |

### Max-heap operation checklist (invariant)


| Operation               | Before                                           | After                                                                 |
| ----------------------- | ------------------------------------------------ | --------------------------------------------------------------------- |
| **Insert**              | Heap is valid                                    | Append at end (keeps complete), then sift-up until order restored     |
| **Delete-max**          | Heap is valid                                    | Swap root with last, remove last, sift-down root until order restored |
| **Heapify / sift-down** | Subtree children are heaps; node `i` may violate | Subtree rooted at `i` is a max-heap                                   |
| **make_heap**           | Arbitrary array                                  | Whole array is a max-heap (complete + order)                          |
| **Heapsort**            | Unsorted array                                   | Sorted ascending (for max-heap version)                               |


**Big idea analogy:** Heap operations are like fixing one student who is in the wrong place in a hierarchy:

- **Insert:** a new student enters at the last seat, then "bubbles up" past less urgent students.
- **Delete-max:** the front student leaves, the last student temporarily takes the front seat, then "sinks down" until both children below are less urgent.
- **Heapify:** a student is sitting too high compared with their children, so they repeatedly swap with the more urgent child.

---



# Day 1 — Representation & Invariants (60–90 min)

**Focus:** Trees + array mapping + formulas + checking heap properties. Little coding; lots of tracing.

## 1.1 Warm-up (10 min)

Answer in your own words (write under each):

1. What two properties make a binary tree a max-heap?
2. Why can we store a heap in an array without wasting space on “missing” children in the middle?
3. Full vs complete — give one example that is complete but not full.



## 1.2 Map tree ↔ list (20 min)

Draw this complete tree, then write the 0-based list:

```text
        50
       /  \
     30    40
    / \   /
  10  20 35
```

Expected list: `[50, 30, 40, 10, 20, 35]`

**Practice:** For each index 0..5, compute parent / left / right (mark “none” if out of range). Check: does every parent ≥ its children?

**Memory trick:** Level-order traversal is the same order as reading classroom seats: front row left to right, then second row left to right, and so on. That is exactly how the heap array is stored.

## 1.3 Spot the violations (15 min)

For each list, say: (a) complete? (b) max-heap order? (c) if not, fix with the *smallest* change you can explain.

1. `[90, 70, 80, 50, 60, 75]`
2. `[90, 80, 70, 85, 60]`  ← order broken somewhere
3. Imagine a tree with a gap on the last level (right child present, left missing) — why can’t that be a heap array?



## 1.4 Implement index helpers (15 min)

Write these yourself (no peeking at solutions later until Day 3):

```python
def parent(i: int) -> int:
    ...

def left(i: int) -> int:
    ...

def right(i: int) -> int:
    ...

def is_max_heap(a: list) -> bool:
    """Return True iff a is a max-heap (order + implied completeness of a list)."""
    ...
```

**Hint for** `is_max_heap`**:** for every `i` with a child index `< n`, check `a[i] >= a[child]`.

## 1.5 Day 1 exit check

- [ ] I can write the three formulas from memory
- [ ] I can convert a drawn complete tree ↔ list
- [ ] I can explain completeness vs heap-order separately
- [ ] Topic checklist: definition, formulas, full vs complete, trees vocab, order & completeness

---



# Day 2 — Implement Insert / Delete / Heapify (60–90 min)

**Focus:** Code the three core primitives. Trace list state beside every swap.

## 2.1 Mental model (5 min)

```text
Insert:     append (complete) → sift UP   (restore order)
Delete-max: swap root↔last, pop → sift DOWN (restore order)
Heapify(i): assume children OK → sift DOWN from i
```

Height of a heap with n nodes is \lfloor\log_2 n\rfloor, so each sift is O(\log n).

**Elevator analogy:**

- `sift_up` is like taking an elevator upward while you have higher priority than your parent.
- `sift_down` is like taking an elevator downward while one of your children has higher priority than you.
- You only move along one path, not through every node, which is why these operations are logarithmic.

## 2.2 Implement sift-up + insert (25 min)

**Coding prompt — write from scratch:**

```python
def sift_up(a: list, i: int) -> None:
    """While a[i] > a[parent], swap and move i up. Stop at root."""
    ...

def insert(a: list, value) -> None:
    """Append value, then sift_up from the new last index."""
    ...
```

**Trace by hand** (write list after each swap):

Start: `[]`  
Insert: `10, 40, 30, 50, 20` one by one into a max-heap.

Example trace:

```text
insert 10: [10]

insert 40:
append:    [10, 40]
sift_up:   [40, 10]          40 beats parent 10

insert 30:
append:    [40, 10, 30]
stop:      [40, 10, 30]      30 does not beat parent 40

insert 50:
append:    [40, 10, 30, 50]
sift_up:   [40, 50, 30, 10]  50 beats parent 10
sift_up:   [50, 40, 30, 10]  50 beats parent 40

insert 20:
append:    [50, 40, 30, 10, 20]
stop:      [50, 40, 30, 10, 20]  20 does not beat parent 40
```

**Analogy:** Insert is like a new player joining a tournament bracket at the bottom. They only challenge their direct parent, then their grandparent, and so on. They do not compare with every player.

After all inserts you should get a valid max-heap (several valid shapes depending on ties/order — check with `is_max_heap`).

## 2.3 Implement sift-down / heapify + delete-max (30 min)

```python
def heapify(a: list, i: int, n: int | None = None) -> None:
    """
    Max-heapify / sift-down.
    n = heap size (may be < len(a) during heapsort).
    Fix subtree rooted at i: repeatedly swap with larger child.
    """
    ...

def delete_max(a: list):
    """
    Remove and return the max (root).
    Empty heap → raise or return None (pick one and stick to it).
    """
    ...
```

**Trace by hand:**

Heap: `[50, 30, 40, 10, 20, 35]`  
Perform `delete_max` twice. After each delete, write the list and verify heap-order.

Example trace for one `delete_max`:

```text
start heap:          [50, 30, 40, 10, 20, 35]
swap root with last: [35, 30, 40, 10, 20, 50]
remove old max:      [35, 30, 40, 10, 20]
sift_down:           [40, 30, 35, 10, 20]  40 is larger child, so swap with 35
```

Returned value: `50`  
Heap after delete: `[40, 30, 35, 10, 20]`

**Analogy:** Delete-max is like the class president leaving the room. To keep the seats complete, the last student moves to the president seat temporarily. Then that student swaps downward with the stronger child until the hierarchy is fair again.

**Edge cases to handle in code:**

- Node with only a left child (no right)
- Leaf node (heapify should do nothing)
- Single-element heap
- Empty heap on delete



## 2.4 Why “heapify” exists (10 min)

Answer:

1. Insert restores order from a **leaf**; heapify restores order from an **internal node** whose children are already heaps.
2. When would you call `heapify(i)` without inserting or deleting? (Hint: Day 3 — building and sorting.)

**Analogy:** Heapify is local repair. Imagine a manager is placed above two teams that are already organized correctly. You only need to check whether that manager belongs above those team leaders. If not, swap them with the stronger leader and continue downward.



## 2.5 Day 2 exit check

- [ ] Insert and delete-max work on paper *and* in code
- [ ] Heapify is iterative (or recursive) and uses `n` as size
- [ ] I can explain O(\log n) from tree height
- [ ] Topic checklist: insert/delete, implementation & underlying DS, heapify

---



# Day 3 — make_heap, Heapsort, Complexities & Quiz (60–90 min)

**Focus:** Build in place, sort, memorize complexities, self-test.

## 3.1 Bottom-up `make_heap` / `build_heap` (20 min)

Leaves are already heaps. Only non-leaves need fixing. Last non-leaf = `n // 2 - 1`. Walk **right → left** toward the root, calling `heapify` on each.

**Analogy:** If every individual desk at the bottom is already "organized" by itself, you do not start fixing from the top blindly. You start from the last small group that has children, fix each group, and eventually the whole classroom hierarchy becomes organized.

```python
def make_heap(a: list) -> None:
    """In-place: turn arbitrary list a into a max-heap using heapify."""
    n = len(a)
    # for i from last_non_leaf down to 0:
    #     heapify(a, i, n)
    ...
```

**Trace:** `a = [10, 20, 15, 30, 40]`

1. `n = 5`, last non-leaf = `5 // 2 - 1 = 1`
2. `heapify` at `i = 1`, then `i = 0`
3. Write the list after each `heapify`

Example trace:

```text
start:       [10, 20, 15, 30, 40]
i = 1:      [10, 40, 15, 30, 20]  40 is larger child of 20
i = 0:      [40, 30, 15, 10, 20]  40 moves to root, then 10 sinks below 30
```

**Why O(n), not O(n\log n)?** Most nodes are near the bottom and sift only a short distance. Summing work over levels gives linear time. (Quiz answer: “most nodes have small height / work decreases geometrically toward the leaves.”)

**Simple analogy for O(n) build:** In a pyramid of students, most students are already near the bottom, so they can only move down a tiny amount. Only a few students near the top can move far. The total work is much less than making every student climb from the bottom one at a time.

**Contrast:** building by repeated `insert` is O(n\log n).

## 3.2 Heapsort (20 min)

Max-heap heapsort → **ascending** order:

1. `make_heap(a)`
2. For `end = n - 1` down to `1`:
  - Swap `a[0]` with `a[end]` (max goes to sorted suffix)
  - `heapify(a, 0, end)`  ← heap size shrinks; do **not** touch the sorted part

```python
def heapsort(a: list) -> None:
    """In-place ascending sort using a max-heap."""
    ...
```

**Trace:** sort `[4, 1, 3, 2, 16, 9, 10, 14, 8, 7]` (or a shorter list like `[5, 1, 4, 2]` if time is short). After each swap + heapify, write the list and mark the sorted region.

**Analogy:** Heapsort is like repeatedly awarding the biggest trophy. The max at the root is the next largest item, so you move it to the back "winner zone." Then you shrink the heap and find the next largest. The back of the array becomes sorted from right to left.

Short example:

```text
start:       [5, 1, 4, 2]
make_heap:   [5, 2, 4, 1]

swap max to end:
             [1, 2, 4, 5]   sorted zone: [5]
heapify 0..2:
             [4, 2, 1, 5]

swap max to end:
             [1, 2, 4, 5]   sorted zone: [4, 5]
heapify 0..1:
             [2, 1, 4, 5]

swap max to end:
             [1, 2, 4, 5]   sorted zone: [2, 4, 5]
done:        [1, 2, 4, 5]
```

## 3.3 Complexity cheat sheet (memorize) (10 min)


| Operation              | Time       | Extra space (typical in-place array heap) |
| ---------------------- | ---------- | ----------------------------------------- |
| Peek max (access root) | O(1)       | O(1)                                      |
| Insert                 | O(\log n)  | O(1)                                      |
| Delete-max             | O(\log n)  | O(1)                                      |
| Heapify / sift-down    | O(\log n)  | O(1) iterative                            |
| make_heap (bottom-up)  | O(n)       | O(1)                                      |
| Build via n inserts    | O(n\log n) | O(1)                                      |
| Heapsort               | O(n\log n) | O(1)                                      |


**Create/Make heap:** if the question means bottom-up `make_heap`, answer O(n). If it means n successive inserts, O(n\log n). Say which you assume.

## 3.4 Concrete test inputs (run your code) (15 min)


| Case             | Input / action                              | What to check                               |
| ---------------- | ------------------------------------------- | ------------------------------------------- |
| Empty            | `delete_max([])`                            | Defined behavior (raise / None)             |
| One item         | `[7]` insert/delete/heapify                 | Still valid; delete leaves `[]`             |
| Duplicates       | `[5, 5, 5, 5]` → make_heap / heapsort       | No crash; sorted `[5,5,5,5]`                |
| Already valid    | `[90, 70, 80, 50, 60]`                      | `is_max_heap` True; make_heap no-op-ish     |
| Sorted ascending | `[1, 2, 3, 4, 5]` → make_heap               | Becomes a max-heap                          |
| Reverse sorted   | `[5, 4, 3, 2, 1]` → make_heap               | Already close to max-heap                   |
| Only left child  | e.g. size 2 or 4 — node with left, no right | heapify/delete handle missing right         |
| Heapsort         | any of the above                            | Ascending order; original heap destroyed OK |




## 3.5 Quiz-style drills (15–20 min)

Do **without** code first, then verify:

1. **Explain:** Why must a heap be complete? What breaks if it isn’t?
2. **Trace:** Insert `45` into `[50, 30, 40, 10, 20, 35]`. Final list?
3. **Trace:** One `delete_max` on the result of (2).
4. **Implement (blank paper):** `heapify` in ~10–15 lines.
5. **Analyze:** Cost of `make_heap` on 1,000,000 elements — O(n) or O(n\log n)? Why?
6. **Debug:** Student code for heapsort calls `heapify(a, 0)` with full `len(a)` every time after swapping. What’s wrong?
7. **Apply:** When is a heap a good choice? (priority queue, repeated get-max, top-k with a heap of size k). When not? (need sorted order of *all* keys often → balanced BST / sort; need search for arbitrary key → hash / BST).



## 3.6 Final self-test rubric


| Skill         | Pass criteria                                                        |
| ------------- | -------------------------------------------------------------------- |
| **Explain**   | Define heap; full vs complete; heap-order; why array storage         |
| **Trace**     | Insert, delete-max, make_heap step, one heapsort pass on ≤8 elements |
| **Implement** | Index helpers + insert + delete_max + heapify + make_heap + heapsort |
| **Analyze**   | Correct complexities from the cheat sheet; O(n) build intuition      |
| **Apply**     | Priority queues / top-k / scheduling vs when *not* to use a heap     |


Check remaining topic checklist boxes when each row above passes.

---



## Optional stretch (if time)

- Flip one comparison to get a **min-heap**; heapsort with min-heap yields descending unless you adapt the swap loop.
- Implement recursive `heapify` and compare stack depth to iterative.
- “Top-k largest”: keep a **min-heap of size k** while scanning — know *why* min-heap, not max-heap.

---



## Study schedule snapshot


| Day   | Time      | Outcome                                         |
| ----- | --------- | ----------------------------------------------- |
| **1** | 60–90 min | Formulas, tree↔array, invariants, `is_max_heap` |
| **2** | 60–90 min | Insert, delete-max, heapify coded + traced      |
| **3** | 60–90 min | make_heap, heapsort, complexities, quiz drills  |


**Rule:** On Days 2–3, write functions blank-paper style first, then type them. Looking up a solution before attempting counts as not done.