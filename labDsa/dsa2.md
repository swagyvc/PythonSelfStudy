```python
# Exercise 1

s = 0 #1
i = 1 #1
while i <= n: # n / 3
    s = s + i  # 2 (n / 3)
    i = i + 3  # 2 (n / 3)

# Exercise 2
s = 0 # 1
i = 1 # 1
while i < n: #log3n + 1
    s = s + i #2(log3n)
    i = i * 3 #2(log3n)

# Exercise 3
s = 0 #1
for i in range(n): #n+1
    for j in range(i): #n(n-1/2)
        s = s + i + j #3n(n-1/2)

# Exercise 4
s = 0 #1
for i in range(1, n): #n
    j = 1 #n
    while j < n: #n log2n
        s = s + i + j #3 n log2n
        j = j * 2 #2 n log2n


# Exercise 5
s = 0 #1
for i in range(n): #n + 1
    for j in range(n): #n (n + 1)
        for k in range(n): #n n (n + 1)
            s = s + i + j + k # 4 n^3
# T(n) = 5n^3 + 2n^2 + 2n + 2
# Iteration n + 1
# O(n^3)

# Exercise 6
i = n #1
while i > 0: #log2(n)
    j = 1 #log2(n)
    while j < n: # log2(n)
        j = j * 2 # 2 log2(n)
    i = i // 2 # 2 log2(n)
#T(n) =
# Iteration:
# log2(n)^2


# Exercise 7
def mystery(arr):
    for i in range(len(arr)): #2(n + 1) => 2n + 2
        for j in range(len(arr)): #n x 2(n+1) => 2n^2 + 2n
            if arr[i] == arr[j]: #n x n => n^2
                return True
    return False #1



# Exercise 8
s = 0 #1
for i in range(n): #n + 1
    j = i #n
    while j > 0: #n x log2(n) + n
        s = s + j # n log2(n) 2
        j = j // 2 # 2 log2(n) n

# Exercise 9
s = 0 # 1
i = 1 # 1
while i < n: # log2(n) + 1
    j = 0 #log2(n)
    while j < i: #n log2(n)
        s = s + j #n n
        j += 1 #n n
    i *= 2 # 2 log2(n)
#


# Exercise 10
s = 0 # 1
for i in range(n): # n + 1
    for j in range(n): #n (n + 1) => n^2 + n 
        k = n # n n => n^2
        while k > 0: #n n log2(n) + 1 => n^2 log2(n) + n^2
            s = s + k #2 * n^2 log2(n) (1 addition, 1 assignment)
            k = k // 2 #2 * n^2 log2(n) (1 addition, 1 assignment)

# T(n) = 5n^2 \log_2(n) + 3n^2 + 2n + 2
# O(n^2log2(n))
```
```py

def one(mylist, key):
	total = 0 #1
	for i in range(len(mylist)):
		for j in range(i+1,len(mylist)):
			if i != j:
				if mylist[i] + mylist[j] == key:
					total += 1
	return total

def two(mylist, key):
	total = 0
	mylist.sort()
	i = 0
	j = len(mylist)-1
	while (i < j):
		if(mylist[i] + mylist[j] < key):
			i+=1
		elif(mylist[i] + mylist[j] > key):
			j-=1
		else:
			total += 1
			i+=1
			j-=1
	return total

def three(mylist, key):
	items={}
	total = 0
	for number in mylist:
		items[number]=1
	for number in mylist:
		other = key-number
		if(other in items):
			total+=1
	return total//2


