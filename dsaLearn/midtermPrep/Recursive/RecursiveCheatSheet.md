# Recursive Base Cases Cheat Sheet

| Input Type / Structure | Smallest Possible Input | Typical Base Case | Common Return Values | Example Problems |
|-----------------------|------------------------|------------------|---------------------|------------------|
| **Number** | `0` or `1` | `if n == 0:`<br>`if n == 1:`<br>`if n <= 0:` | `0`, `1`, `True`, `False` | Factorial, Fibonacci, Sum 1..n |
| **String** | Empty string `""` | `if len(s) == 0:` | `""`, `0`, `True` | Reverse String, Palindrome |
| **Array / List** | Empty list `[]` | `if len(arr) == 0:` | `[]`, `0`, `False` | Sum Array, Search Array |
| **Linked List** | `None` node | `if node is None:` | `0`, `False`, `None` | Length, Search, Traversal |
| **Binary Tree** | Empty node (`None`) | `if root is None:` | `0`, `False`, `[]` | Height, DFS, Sum Nodes |
| **Binary Search** | Search space exhausted | `if left > right:` | `-1`, `False` | Binary Search |
| **Graph DFS** | Already visited node | `if node in visited:` | `None` | DFS, Connected Components |
| **Backtracking** | Solution found or invalid state | `if solution_found:`<br>`if invalid_state:` | `return`, `True`, `False` | N-Queens, Sudoku, Permutations |

---

## Quick Interview Mapping

| Question Asks For... | Typical Base Return |
|----------------------|--------------------|
| Sum | `0` |
| Product | `1` |
| Count | `0` |
| Build String | `""` |
| Build List | `[]` |
| Boolean Check | `True` / `False` |
| Search Result | `False` or `-1` |
| Tree Height | `0` |
| Path Count | `1` or `0` (depends on problem) |

---

## Universal Formula

| Step | Question to Ask |
|--------|----------------|
| 1 | What is the smallest valid input? |
| 2 | What answer should that smallest input return? |
| 3 | How do I reduce the current problem toward that smaller input? |
| 4 | How do I combine the recursive result with the current state? |

> **Base Case = Smallest Solvable Problem**  
> **Recursive Case = Current Problem → Smaller Version of Itself**