# Reflection for Lab 3

## Part A: Analysis

### function 1:

```python
def function1(value, number):
	if (number == 0): #1
		return 1
	elif (number == 1): #1
		return value
	else:
		return value * function1(value, number-1) #T(n - 1) + 2


#T(n) = 1 + 1 + 2 + T(n - 1) = 4 + T(n - 1)
#T(n - 1) = 4 + T(n - 2)
#T(n - 2) = 4 + T(n - 3)
#...
#T(n) = 4 + T(n - 1)
#     = 4 + 4 + T(n - 2)
#     = 4 + 4 + 4 + T(n - 3)
#     = 4 + 4 + 4 + ... + T(0) = 4 + 4 + 4 + ... + 2 = 4(n - 1) + 2
#     = 4n - 4 + 2 = 4n - 2
#T(n) = 4n - 2
#T(n) is O(n)
```

### function 2:

```python

def recursive_function2(mystring,a, b):
	if(a >= b ): #1
		return True
	else:
		if(mystring[a] != mystring[b]): #1
			return False
		else:
			return recursive_function2(mystring,a+1,b-1) #T(n - 2) + 2

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)#4n - 6 + 1 = 4n - 5 => T(n) = 4n - 5 => T(n) is O(n)


#T(n) = 1 + 1 + 2 + T(n - 2) = 4 + T(n - 2)
#T(n - 2) = 4 + T(n - 4)
#T(n - 4) = 4 + T(n - 6)
#...
#T(n) = 4 + T(n - 2)
#     = 4 + 4 + T(n - 4)
#     = 4 + 4 + 4 + T(n - 6)
#     = 4 + 4 + 4 + ... + T(0) = 4 + 4 + 4 + ... + 2 = 4(n - 2) + 2
#     = 4n - 8 + 2
#T(n) = 4n - 6
#T(n) is O(n)
```

### function 3 (optional):

```python
def function3(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		half = number // 2
		result = function3(value, half)
		if (number % 2 == 0):
			return result * result
		else:
			return value * result * result

```

## Part C reflection
