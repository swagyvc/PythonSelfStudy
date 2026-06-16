Here are some practice exercises that include recursive functions, following the same markdown format.

### Exercise 9: Simple Reduction Recursion

```python
def fun(n):
    if n <= 1:
        return 1
    s = 0
    for i in range(n):
        s = s + i
    return fun(n - 1)

```

* **Find:** $T(n)$ and Big O

---

### Exercise 10: Binary Splitting Recursion

```python
def fun(n):
    if n <= 1:
        return 1
    s = 0
    for i in range(n):
        s = s + i
    return fun(n // 2) + fun(n // 2)

```

* **Find:** $T(n)$ and Big O

---

### Exercise 11: Logarithmic Step Recursion

```python
def fun(n):
    if n <= 1:
        return 1
    i = 1
    while i < n:
        i = i * 2
    return fun(n - 1)

```

* **Find:** $T(n)$ and Big O

---

### Solutions

#### Exercise 9

* **$T(n)$ Calculation:** The work done at each level is $O(n)$ due to the loop. The function reduces $n$ by 1 each time, leading to $n$ recursive calls. Total work is $n + (n-1) + (n-2) + \dots + 1 = \frac{n(n+1)}{2}$.
* **Big O:** $O(n^2)$

#### Exercise 10

* **$T(n)$ Calculation:** Each level of the recursion tree splits into 2 branches but halves the input size. The work done at the root is $O(n)$. At the next level, it is $2 \times O(\frac{n}{2}) = O(n)$. The total work at each level of the tree remains $O(n)$, and there are $\log n$ levels.
* **Big O:** $O(n \log n)$

#### Exercise 11

* **$T(n)$ Calculation:** The internal loop takes $O(\log n)$ time. The function reduces $n$ by 1 each time, running $n$ times. Total work is $\sum_{i=1}^{n} \log i = \log(n!) \approx n \log n$.
* **Big O:** $O(n \log n)$