```py
def f(n):
    if n <= 1: #1
        return 1 #0
    return f(n - 1) #1 + T(n - 1)

```
Basecase: T(0) = 1
          T(1) = 1

T(n)     = 2 + T(n - 1)
T(n - 1) = 2 + T(n - 2)
T(n - 2) = 2 + 2 + T(n - 3)

=> T(n) = 2 + 2 + 2 + ... + 1
T(n) = 2(n - 1) + 1 = 2n - 2 + 1
T(n) = 2n - 1
T(n) is O(n)

