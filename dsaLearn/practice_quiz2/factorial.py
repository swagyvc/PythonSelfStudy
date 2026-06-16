def factorial(n): #T(n)
    if n > 0: #1
        return n * factorial(n- 1) #2 + T(n - 1)
    else:
        return False

#  T 

x = factorial(-10)
print(x)