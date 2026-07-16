# Lab 5

This assessment contains materials that may be subject to copyright and other intellectual property rights. 

Modification, distribution or reposting of this document is strictly prohibited. Learners found reposting this document or its solution anywhere will be subject to the college’s Academic Integrity policy.

## Due: 

* In class Component due at the end of your lab period when this lab is assigned
* Coding Component due Sunday after the in class component

## Objectives:

In this lab you will look at Heaps and Heap Sort

## Setup 

### Repo

The repo you created in lab 1 is used for all labs this semester.

### In Class

- Find a partner or two
- On the sheet of paper given to you write your name
- **Each person must submit their own sheet**
- Work on the following problem.  If you need extra sheets of paper, please let me know.
- Explanations can be done verbally, no need to write it down...

## Part A - In Class
   
### Heap Insertion:

Each person in team takes turn explaining how to inserting the values below into an initially empty minheap.  Draw the heap after each insertion.

10, 6, 5, 4, 9, 16, 7, 18, 22, 1, 3, 8, 2, 11


### Heap Removal

Suppose you are giving the following array representation of a heap.:

[60, 30, 36, 20, 22, 27, 15, 14, 17, 21, 5, 24, 26, 6, 12, 11, 3, 10, 9, 13, 16]

1. Draw the heap
2. Each person in the group explains how to remove a value from the heap.  Draw the heap after each removal. Each person demonstrates how to do removal twice (so if you have team of 3, you have to remove 6 values, a team of 2 removes 4 values)


### Make Heap

Suppose you were givent the following array:

[11, 2, 5, 6, 7, 8, 9, 12, 4, 10, 1, 3, 15, 13, 14]

1. Draw the complete binary tree represented by the array above
2. Each person in the team takes a turn performing heapify on a value, explain how it works (starting with first non leaf from the back) do this until we end up with a maxheap.
3. Redraw heap after each heapify operation.

### Heap Sort

Start with the maxheap you have from the makeheap section

- what is the array form of the heap?
- Each person in the team will take turn doing the following:
  1. Swap root with bottom right most node
  2. Percolate down the element you have at the root (note that doing this process, you should ignore the elements you have already moved/swapped to the end of the array; they are gradually shaping the sorted partition!)
- write the array form of the heap after each number gets processed
- Do this until you have a sorted array (sorted in ascending order)

## Part B - Programming:


In this section of the lab, you will implement a class for a MinHeap (smaller values have higher priority). Use the array implementation as discussed in class for your implementation.

When the MinHeap is instantiated, it may be passed an list.  If a list is provided, your program will create a duplicate of the list and apply the make_heap() algorithm to turn the list into a min heap.

If no list is provided the min heap begins empty.

---

```python  
def is_empty(self):
```
This function returns True if the heap is empty false otherwise

---
```python  
def size(self):
```
This function returns number of items stored in the heap

---


```python
def push(self, data):
```
This function adds data to the heap

---

```python
def pop(self):
```
This function removes and returns the smallest item from the heap.  Function does nothing and returns None if heap is empty

---

```python  
def min(self):
```
This function returns the smallest item from the heap.  Function returns None if heap is empty

---





## Lab Rubric:

| Criteria       | Poor - 0 mark     | Fair - 1 marks                                                                                                                     | Good - 2 marks                                                              |
| -------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| Lab Completion | Part A not completed | Either Part A (In class) or Part B (Programming) was incomplete | Successfully All parts portions |