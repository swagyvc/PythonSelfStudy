Here are some practice exercises that include recursive functions, following the same markdown format.

### Exercise 9: Simple Reduction Recursion

```md
    ```py
    def fun(n): #T(n)???
        if n <= 1: #1
            return 1#0
            s = 0 #1
        for i in range(n): #n + 1
            s = s + i #n * 2
            return fun(n - 1) #n * 1 * T(n - 1)
    ```
T(n) = 3 + 5n + n * T(n - 1)
T(n - 1) = 3 + 5n + n * T(n - 2)
T(n - 2) = 3n + 5n + n * T(n - 3)
...
T(n) = 3 + 5n + n * T(n - 1)
     = 3 + 5n + 3 + 5n + n * T(n - 2)
     = 3 + 5n + 3 + 5n + 3 + 5n + n * T(n - 3)
     = 3 + 5n + 3 + 5n + .....  + n * T(0)
     = 3 + 5n + 3 + 5n + .....  + n * 2
     = (3 + 5n)(n - 1) + .....  + n * 2
     = 3n - 3 + 5n^2 - 5 + 2n
     = 5n^2 - 3
T(n) = O(n^2)
```

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