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
---

### Exercise 2: Decrementing Division Loop

```python
s = 0  #1
i = n  #1
while i > 1:  #log_3(n) - 1
    s = s + i   #log_3(n) + 2
    i = i // 3  #log_3(n) + 2

```
T(n) = 3log_3(n) + 5
T(n) is O(logn)

* **Find:** $T(n)$ and Big O

---

### Exercise 3: Double Nested Loop

```python
s = 0  #1
for i in range(n): #n + 1
    for j in range(n): # n (n + 1)
        s = s + i + j  # n n 3

```
T(n) = 1 + n + 1 + n^2 + n + 2n + 3
T(n) = 5 + 4n + n^2
T(n) is O(n^2)

* **Find:** $T(n)$ and Big O

---

### Exercise 4: Nested Loop with Multiplication

```python
s = 0  #1
for i in range(n): #n + 1
    k = 1  #n + 1
    while k < n: #n (n - 1)
        s = s + i + k #n (n) 
        k = k * 2  #n 

```

* **Find:** $T(n)$ and Big O

---

### Solutions

#### Exercise 1

* **$T(n)$ Calculation:** First loop: $1 + 1 + n + 2(n-1) + 2(n-1) = 5n - 2$
Second loop: $1 + \frac{n}{2} + 2(\frac{n}{2}-1) + 2(\frac{n}{2}-1) = \frac{5n}{2} - 3$
Total $T(n) = (5n - 2) + (\frac{5n}{2} - 3) = 7.5n - 5$
* **Big O:** $O(n)$

#### Exercise 2

* **$T(n)$ Calculation:** $T(n) = 1 + 1 + \log_3(n) + 2\log_3(n) + 2\log_3(n) = 2 + 5\log_3(n)$
* **Big O:** $O(\log n)$

#### Exercise 3

* **$T(n)$ Calculation:** $T(n) = 1 + (n + 1) + n(n + 1) + 3n^2 = 4n^2 + 2n + 2$
* **Big O:** $O(n^2)$

#### Exercise 4

* **$T(n)$ Calculation:** Outer loop runs $n$ times. Inner loop runs $\log(n)$ times.
$T(n) = 1 + (n + 1) + n(1 + \log n) + 4n\log n = 5n\log n + 2n + 1$
* **Big O:** $O(n\log n)$