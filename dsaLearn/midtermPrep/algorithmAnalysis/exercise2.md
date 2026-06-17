Here is another batch of exercises in the exact same style.

### Exercise 5: Single Triple-Step Loop

```python
s = 0 #1
i = 1  #1
while i < n: #n/3 + 1
    s = s + i   #n/3 * 2 = 2/3n
    i = i + 3   #n/3 * 2 = 2/3n

```
T(n) = 5/3n + 3
T(n) is O(n)
---

### Exercise 6: Three Sequential Loops

```python
s = 0  #1
for i in range(n): #n + 1 
    s = s + i  #2 * n = 2n

for j in range(n): #n + 1
    s = s + j  #n * 2= 2n

k = 1  #1
while k < n: #log_2(n) + 1 
    s = s + k  #log_2(n) * 2
    k = k * 2  #log_2(n) * 2

```
T(n) = 4log_2(n) + 6n + 5
T(n) is Olog(n)

---

### Exercise 7: Nested Loop with Subtraction

```python
s = 0  # 1
for i in range(n): # n + 1
    j = n # n
    while j > 1: # n * n = n^2  (runs n times per outer loop)
        s = s + i + j # n * (n - 1) * 3 = 3n^2 - 3n
        j = j - 1  # n * (n - 1) * 2 = 2n^2 - 2n

```
$$T(n) = 1 + (n + 1) + n + n^2 + (3n^2 - 3n) + (2n^2 - 2n)$$

$$T(n) = 6n^2 - 3n + 2$$

---

### Exercise 8: Highly Nested Multiplication Loop

```python
s = 0 #1 
for i in range(n): #n + 1
    for j in range(n): #n * (n + 1) = n^2 + n
        s = s + i + j #n * n * 3 = 3n^2

#first block = 4n^2 + 2n + 2

for k in range(n): #n + 1
    m = 1  #n * 1 = n
    while m < n: #n * (log_3(n) + 1) = log_3(n^2) + n
        s = s + k + m  #n * log_3(n) * 3 = 3log_3(n^2)
        m = m * 3  #n * log_3(n) * 2 = 2log_3(n^2)

```
$$T(n) = 4n^2 + 6n\log_3 n + 6n + 4$$

$$T(n) is O(log(n^2))$$