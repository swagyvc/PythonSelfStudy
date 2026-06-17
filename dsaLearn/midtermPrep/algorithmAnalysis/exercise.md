### Exercise 1: Sequential Loops

```python
s = 0          # 1
i = 0          # 1
while i < n:   # n + 1 (checks 0 to n)
    s = s + i  # 2n (1 add, 1 assign per iteration)
    i = i + 1  # 2n (1 add, 1 assign per iteration)

j = 0          # 1
while j < n:   # (n/2) + 1
    s = s + j  # 2 * (n/2) = n
    j = j + 2  # 2 * (n/2) = n

```
$$T(n) = 1 + 1 + (n + 1) + 2n + 2n + 1 + \left(\frac{n}{2} + 1\right) + n + n$$

$$T(n) = 6.5n + 5$$

$$Big O: O(n)$$
---

### Exercise 2: Decrementing Division Loop

```python
s = 0          # 1
i = n          # 1
while i > 1:   # log_3(n) + 1
    s = s + i  # 2 * log_3(n)
    i = i // 3 # 2 * log_3(n) (1 floor div, 1 assign)
```
$$T(n) = 1 + 1 + (\log_3 n + 1) + 2\log_3 n + 2\log_3 n$$

$$T(n) = 5\log_3 n + 3$$

$$Big O: O(\log n)$$

---

### Exercise 3: Double Nested Loop

```python
s = 0              # 1
for i in range(n): # n + 1
    for j in range(n): # n * (n + 1) = n^2 + n
        s = s + i + j  # n * n * 3 = 3n^2
```
$$T(n) = 1 + (n + 1) + (n^2 + n) + 3n^2$$

$$T(n) = 4n^2 + 2n + 2$$

$$Big O: O(n^2)$$


### Exercise 4: Nested Loop with Multiplication

```python
s = 0  #1
for i in range(n): #n + 1
    k = 1  #n * 1 = n
    while k < n: #n * (log_2(n) + 1) = n log_2(n) + n
        s = s + i + k # n * log_2(n) * 3 = 3n log_2(n)
        k = k * 2 # n * log_2(n) * 2 = 2n log_2(n)
```
$$T(n) = 1 + (n + 1) + n + (n\log_2 n + n) + 3n\log_2 n + 2n\log_2 n$$

$$T(n) = 6n\log_2 n + 3n + 2$$

$$Big O: O(n \log n)$$