Here is the markdown formatted version containing the exercises, followed by a hidden section with the answers so you can test yourself.

### Exercise 1: Sequential Loops

```python
s = 0  
i = 0  
while i < n:  
    s = s + i   
    i = i + 1   

j = 0  
while j < n:  
    s = s + j   
    j = j + 2   

```

* **Find:** $T(n)$ and Big O

---

### Exercise 2: Decrementing Division Loop

```python
s = 0  
i = n  
while i > 1:  
    s = s + i   
    i = i // 3  

```

* **Find:** $T(n)$ and Big O

---

### Exercise 3: Double Nested Loop

```python
s = 0  
for i in range(n):  
    for j in range(n):  
        s = s + i + j  

```

* **Find:** $T(n)$ and Big O

---

### Exercise 4: Nested Loop with Multiplication

```python
s = 0  
for i in range(n):  
    k = 1  
    while k < n:  
        s = s + i + k  
        k = k * 2  

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