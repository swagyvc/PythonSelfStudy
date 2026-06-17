# # Exercise 1: String Reversal (Sequence Pattern)
# # Write a recursive function reverse_string(s) that takes a string s and returns it reversed.
# # Example: reverse_string("apple") should return "elppa".
# # Hint: Think about how to combine the last character or the first character with the recursive result of the rest of the string.
def reverseString(text):
    if len(text) == 0: #base case
        return 0
    #continue
    

# Exercise 2: Count Even Numbers (Sequence Pattern)
# Write a recursive function count_evens(numbers) that takes a list of integers and returns the total count of even numbers in that list.
# Example: count_evens([2, 5, 8, 10, 11]) should return 3.
# Hint: Look at numbers[0]. If it's even, add 1 to the recursive result of numbers[1:]. If it's odd, add 0.


# Exercise 3: Recursive Power Function (Number Pattern)
# Write a recursive function power(base, exp) that calculates $\text{base}^{\text{exp}}$ without using the  operator or any loops. 
# Assume exp is an integer $\ge 0$.Example: power(2, 3) should return 8.
# Hint: Your base case is when exp == 0. Your recursive step should decrement exp by 1.


# Exercise 4: Clean String (Advanced Trapping Pattern)
# Write a recursive function clean_string(s) that takes a string and returns a new string where adjacent duplicate characters are reduced to a single character.
# Example: clean_string("yyyees") should return "yes".
# Hint: Your base case changes here. You need to check if the string has a length of 0 or 1. If it's longer, compare s[0] with s[1].