# Example 0
s = 0 #1
i = 1 # 1
while i < n: # n
    s = s + i # 2(n - 1)
    i = i + 1 #2 (n - 1)

#T(n) = 5n - 2
#T(n) is O(n)

#============================
s = 0 # 1
i = 1 #  1

while i < n: # log(n)
    s = s + i # 2log(n)
    i = i * 2 # 2log(n)

#T(n) = 2 + 5log(n)
#T(n) is O(log(n))
#============================

s = 0 #1
i = n #1

while i > 1: #log(n)
    s = s + i #2log(n)
    i = i // 2 #2log(n)

#T(n) = 2 + 5log(n)
#T(n) is O(log(n))

#============================

s = 0 #1

for i in range(n): #n + 1
    for j in range(n): #n * n +1 
        s = s + i + j # 3 * n * n

#T(n) = 1 + n + 1 + n^2 + n + 3n^2 = 4n^2 + n + 1
#T(n) is O(n^2)

#============================

s = 0 #1

for i in range(0, n, 2): #n/2 + 1
    for j in range(n): #n/2*(n + 1)
        s = s + i + j #3*n*n/2

# T(n) 


#============================

s = 0 #1

for i in range(0, n, -1): #n + 1 (but it will never run because the step is negative and the start is less than the end)
    for j in range(n):# n (n + 1)
        s = s + i + j# 3 n n

#T(n) = 1 + n + 1 + n (n + 1) + 3 n n = O(n^2)
#T(n) is O(n^2)
#============================

def linear_search(arr, target): 
    for i in range(len(arr)): #n + 1 + 1
        if arr[i] == target: #n
            return i #0
    return -1 #1

#T(n) = 2n + 3 
#T(n) is O(n)


#============================
s = 0 #1

for i in range(n): #
    for j in range(n):#
        k = 1 #

        while k < n: #
            s = s + i + j + k #
            k = k * 2 #

