#function 2 sum that receive 2 paramaters and return the sum of them
```py
def sum(a,b):
    if type(a) is not str and type(b) is not str:
        result = a + b
        print(f"Result: {result}")
    else:
        print("A or B is a string! Please try again!")

number1 = int(input("Enter number A: "))
number2 = int(input("Enter number B: "))

sum(number1,number2)

```

#Python Basics (Control Flow & Loops)
Task: Write a program that prints the numbers from 1 to 20. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

draft
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
        F     F     F       F     ...
            B         B              B    

```py
for i in range(1,20 + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
```

### Exercise 5: Reverse a String
Task: Write a program that takes a string and prints it in reverse order using a loop.

Input: "python"
Output: "nohtyp"

Draft
['p', 'y', 't', 'h', 'o', 'n']
  0    1    2    3  ....

```python
data = "python"
reverseData = data[::-1]
print(reverseData)
```

### Exercise 6: Find the Maximum Number
Task: Given a list of numbers, use a for loop to find and print the largest number in the list. Do not use the built-in max() function.
Input: [4, 12, 9, 2, 21, 7]
Output: 21

if 4 < 12
-> maxNum 12
12 < 9
-> maxNum 12
12 < 2
-> maxNum 12
12 < 21
-> maxNum 21
21 < 7
-> maxNum 21

```py
lst = [4, 12, 9, 2, 21, 7]
maxNum = 0
for i in range(len(lst)):
    if lst[i] > maxNum:
        maxNum = lst[i]
print(maxNum)
```

### Exercise 7: Even and Odd Split
Task: Write a program that iterates through a list of numbers and separates them into two new lists: one for even numbers and one for odd numbers. Print both lists at the end.

Input: [1, 2, 3, 4, 5, 6]
Output: Even: [2, 4, 6], Odd: [1, 3, 5]

noted: An even number is a whole number that can be divided exactly by 2 with no remainder.
An odd number is a whole number that leaves a remainder of 1 when divided by 2.

```python
lst = [1, 2, 3, 4, 5, 6]
even = []
odd = []
for i in range(len(lst)):
    if lst[i] % 2 == 1: #odd
        odd.append(lst[i])
    elif lst[i] % 2 == 0: #even
        even.append(lst[i])  
print(f"Even: {even} Odd: {odd} ") 
```

### Exercise 8: Sum of a List
Task: Write a program that takes a list of numbers and calculates the total sum of all the elements using a for loop. Do not use the built-in sum() function.

Input: [5, 10, 15, 20]
Output: 50

```py
num_list = [5, 10, 15, 20]
result = 0
for i in range(len(num_list)):
    result += num_list[i]
print(result)
```

### Exercise 9: Remove Duplicates
Task: Given a list with duplicate elements, write a program that creates a new list with the duplicates removed. Keep the original order of the elements.

Input: [1, 2, 2, 3, 4, 4, 5]
Output: [1, 2, 3, 4, 5]
```py
num_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for i in num_list:
    if not unique_list or i !=  unique_list[-1]:
        unique_list.append(i)
print(unique_list)
```

### Exercise 10: Palindrome Checker
Task: Write a program that checks if a given word is a palindrome (reads the same backward as forward). Print True if it is, and False if it is not.

Input: "radar" (Output: True)
Input: "python" (Output: False)

split words
r a d a r
0 1 2 3 4
if first index = last index
if sencond index = last index - 1

did.
deed.
civic.
pop.
eye.
rotor.
radar.
nun.

```python
words = input("Enter a word: ")
new_list = list(words)
#new_list = ['d','e','e','d']
#             0   1.  2.  3
count_back = new_list[::-1]

def palindrome(wrd):
    for i in range(len(new_list)):
        if new_list[i] == count_back[i]:
            return print("True")
        elif new_list[i] != count_back[i]:
            return print("False")
        
palindrome(words)
```
