Here is another batch of exercises in the exact same style.

### Exercise 5: Single Triple-Step Loop

```python
s = 0  
i = 1  
while i < n:  
    s = s + i   
    i = i + 3   

```

* **Find:** $T(n)$ and Big O

---

### Exercise 6: Three Sequential Loops

```python
s = 0  
for i in range(n):  
    s = s + i  

for j in range(n):  
    s = s + j  

k = 1  
while k < n:  
    s = s + k  
    k = k * 2  

```

* **Find:** $T(n)$ and Big O

---

### Exercise 7: Nested Loop with Subtraction

```python
s = 0  
for i in range(n):  
    j = n  
    while j > 1:  
        s = s + i + j  
        j = j - 1  

```

* **Find:** $T(n)$ and Big O

---

### Exercise 8: Highly Nested Multiplication Loop

```python
s = 0  
for i in range(n):  
    for j in range(n):  
        s = s + i + j  
        
for k in range(n):  
    m = 1  
    while m < n:  
        s = s + k + m  
        m = m * 3  

```

* **Find:** $T(n)$ and Big O

---

### Solutions

#### Exercise 5

* **$T(n)$ Calculation:** The loop increments by 3 each time, so it executes $\frac{n}{3}$ times.
$T(n) = 1 + 1 + \frac{n}{3} + 2(\frac{n}{3}-1) + 2(\frac{n}{3}-1) = \frac{5n}{3} - 2$
* **Big O:** $O(n)$

#### Exercise 6

* **$T(n)$ Calculation:** Loop 1 is $5n-2$. Loop 2 is $5n-2$. Loop 3 is $2+5\log(n)$.
Total $T(n) = 1 + (5n-2) + (5n-2) + (2+5\log n) = 10n + 5\log n - 1$
* **Big O:** $O(n)$

#### Exercise 7

* **$T(n)$ Calculation:** Outer loop runs $n$ times. Inner loop decrements by 1 from $n$ to 1, running $n$ times lineally.
$T(n) = 1 + (n+1) + n(1+n) + 4n^2 = 5n^2 + 2n + 2$
* **Big O:** $O(n^2)$

#### Exercise 8

* **$T(n)$ Calculation:** The first block is a double nested loop: $4n^2 + 2n + 2$.
The second block is a loop running a log loop: $5n\log_3 n + 2n + 1$.
Total $T(n) = 4n^2 + 5n\log_3 n + 4n + 3$
* **Big O:** $O(n^2)$ (since $n^2$ grows faster than $n\log n$)