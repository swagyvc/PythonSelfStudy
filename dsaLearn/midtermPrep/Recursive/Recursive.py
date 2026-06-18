# # Exercise 1: String Reversal (Sequence Pattern)
# # Write a recursive function reverse_string(s) that takes a string s and returns it reversed.
# # Example: reverse_string("apple") should return "elppa".
# # Hint: Think about how to combine the last character or the first character with the recursive result of the rest of the string.

# def reverseString(text):
#     if len(text) == 0: #base case
#         return ""
#     return reverseString(text[1:]) + text[0]

# user = input("Enter words: ")
# print(reverseString(user))

# reverseString("cat")
# │
# ├─ reverseString("at") + "c"
# │
# └── reverseString("at")
#     │
#     ├─ reverseString("t") + "a"
#     │
#     └── reverseString("t")
#         │
#         ├─ reverseString("") + "t"
#         │
#         └── reverseString("")
#             │
#             └─ returns ""


# Exercise 2: Count Even Numbers (Sequence Pattern)
# Write a recursive function count_evens(numbers) that takes a list of integers and returns the total count of even numbers in that list.
# Example: count_evens([2, 5, 8, 10, 11]) should return 3.
# Hint: Look at numbers[0]. If it's even, add 1 to the recursive result of numbers[1:]. If it's odd, add 0.

# number = [2, 5, 8, 10, 11]

# def evenCheck(num):
#     # 1. Base Case: An empty list has 0 even numbers
#     if len(num) == 0:
#         return 0

#     # 2. Work & Recursive Step
#     if num[0] % 2 == 0:
#         # If it's even count it as 1 and check the rest
#         return 1 + evenCheck(num[1:])
#     else:
#         # if it's odd count it as 0 and check the rest
#         return 0 + evenCheck(num[1:])

# print(evenCheck(number))

# Exercise 3: Recursive Power Function (Number Pattern)
# Write a recursive function power(base, exp) that calculates $\text{base}^{\text{exp}}$ without using the  operator or any loops. 
# Assume exp is an integer $\ge 0$.Example: power(2, 3) should return 8.
# Hint: Your base case is when exp == 0. Your recursive step should decrement exp by 1.


# Exercise 4: Clean String (Advanced Trapping Pattern)
# Write a recursive function clean_string(s) that takes a string and returns a new string where adjacent duplicate characters are reduced to a single character.
# Example: clean_string("yyyees") should return "yes".
# Hint: Your base case changes here. You need to check if the string has a length of 0 or 1. If it's longer, compare s[0] with s[1].

    

# def check(text):
#     # 1. Base Case: 0 or 1 letters left means it's a palindrome
#     if len(text) <= 1:
#         return True
        
#     # 2. Work: Check if the outer letters match
#     if text[0] == text[-1]:
#         # 3. Leap of Faith: Check the inner remaining slice
#         return check(text[1:-1])
        
#     # If outer letters don't match, it's not a palindrome
#     return False

# # Test it
# print(check(["p","e","e","p"])) # Returns True
# print(check(["a","p","p","l","e"])) # Returns False

#Sum
# number = 4
# def sum_to_end(n):
#     if n == 1:
#         return 1
#     return n + sum_to_end(n - 1)

# print(sum_to_end(number))

#=====Factorial=====
#Recursion
# number = 5
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(number))

#Iterative
# number = 5
# def factorial(n):
#     if n <= 0:
#         return 1
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# print(factorial(number))
#=====================



