## DSA Exam Ultimate Cheat Sheet: Hash Tables & Modulo

## 1. Manual Modulo Calculation (No Calculator)
The modulo operation ($A \pmod B$) finds the remainder left over after dividing integer $A$ by integer $B$.
## Step-by-Step Algorithm

   1. Divide: Divide $A$ by $B$. Drop the decimals to find the whole-number quotient.
   2. Multiply: Multiply that whole number by $B$.
   3. Subtract: Subtract that result from your original $A$. This is your answer.

## Example: $29 \pmod 6$

   1. $29 \div 6 = 4.833 \rightarrow$ Keep the $4$
   2. $6 \times 4 = 24$
   3. $29 - 24 =$ 5

## Shortcut Rules

* Mod 2: If the number ends in $0, 2, 4, 6, 8$, ans $= 0$. If it ends in $1, 3, 5, 7, 9$, ans $= 1$.
* Mod 5: Look at the last digit. If it is $< 5$, that is your answer. If it is $\ge 5$, subtract $5$ from it.
* Mod 10: The answer is always just the very last digit of the number.
* Negative Modulo ($-A \pmod B$): Find the positive mod first ($A \pmod B = R$), then subtract that remainder from the divisor ($B - R$).
* Example: $-2 \pmod 5 \rightarrow (5 - 2) =$ 3

## 2. Load Factor Formula ($\alpha$)
The load factor measures how full the hash table is. It determines when performance will degrade and when resizing (rehashing) is required.

$$\alpha = \frac{n}{m}$$

* $n$ = Total number of items currently inserted in the table.
* $m$ = Total size of the hash table (number of slots/buckets).

Example:

* Scenario: You are given an empty hash table with an array size of \(m = 10\). You insert the keys 14, 25, 36, 47, 58, 69.

1. Count the items $(n)$: There are 6 keys in total.
2. Identify the table slots $(m)$: The array has 10 slots.
3. **Calculate**: 
$$(alpha =\frac{6}{10}=0.6)$$

## Threshold Behaviors

* Chaining: $\alpha$ can be greater than $1$ (slots can hold lists with multiple elements).
* Open Addressing: $\alpha$ can never exceed $1$. Performance drops drastically when $\alpha > 0.7$, triggering a rehash.

## 3. Collisions & Resolution Strategies
A collision occurs when two distinct keys generate the exact same index via the hash function ($h(k_1) = h(k_2)$).
## Category 1: Chaining (Open Hashing)

* Each table slot points to the head of a linked list.
* Collisions are resolved by appending or prepending the new item to the list at that index.
* Worst-case: $O(n)$ if all keys hash to the exact same slot.

## Category 2: Open Addressing (Closed Hashing)
- All items are stored directly within the hash table array. If a slot is occupied, the algorithm "probes" (searches) for the next available slot according to a specific pattern.

## 4. Probing Methods (Open Addressing)## A. Linear Probing
Checks sequential slots one by one until an empty slot is found.

$$\text{Probe Index} = (h(k) + i) \pmod m \quad \text{for } i = 0, 1, 2, 3\dots$$

* Flaw: Suffers from Primary Clustering (long, contiguous blocks of occupied slots build up, slowing down searches).

## B. Quadratic Probing
Checks slots using a squared interval step to eliminate primary clustering.

$$\text{Probe Index} = (h(k) + i^2) \pmod m \quad \text{for } i = 0, 1, 2, 3\dots$$

* Sequence: $h(k)$, $\;h(k)+1$, $\;h(k)+4$, $\;h(k)+9 \dots$
* Flaw: Suffers from Secondary Clustering (keys that hash to the same initial index will follow the exact same probing sequence path).

## C. Double Hashing
Uses a secondary hash function ($h_2(k)$) to determine the step-size interval. This is the most efficient probing method.

$$\text{Probe Index} = (h(k) + i \cdot h_2(k)) \pmod m \quad \text{for } i = 0, 1, 2, 3\dots$$

* Rule: $h_2(k)$ must never output $0$, otherwise the probe will get stuck in an infinite loop.

## 5. Tombstoning (Lazy Deletion)
In Open Addressing, you cannot simply wipe out data or leave a deleted slot empty (null). Doing so breaks the lookup path for keys inserted after that element collided.
## The Fix: Lazy Deletion

* When an item is removed, place a dummy marker called a Tombstone (often marked as DELETED or -1) in that slot.
* Insertion Logic: Treats a tombstone as an empty slot and can overwrite it with new data.
* Searching Logic: Treats a tombstone as an occupied slot and safely continues probing past it to find the intended key.

## 6. Core Operations Logic (Open Addressing)

graph TD
    A[Start Operation] --> B{What Operation?}
    B -->|Insertion| C[Probe table slots]
    C --> D{Is slot Empty or Tombstone?}
    D -->|Yes| E[Insert Key & Stop]
    D -->|No| F[Move to next probe index]
    
    B -->|Searching| G[Probe table slots]
    G --> H{Is slot Empty?}
    H -->|Yes| I[Key not found & Stop]
    H -->|No| J{Does key match?}
    J -->|Yes| K[Return Key & Stop]
    J -->|No| L[Move to next probe index including Tombstones]

## Insertion

   1. Calculate the initial index using $h(k)$.
   2. If the slot is occupied, use your probing method ($i = 1, 2, 3\dots$) to find the first Empty or Tombstone slot.
   3. Place the item and increment your item count ($n$).

## Searching

   1. Calculate the initial index using $h(k)$.
   2. Look at the slot. If it matches the key, return it.
   3. If the slot contains a different key or a Tombstone, keep probing.
   4. Stop and return "Not Found" only if you hit a truly Empty (null) slot.

## Removal

   1. Perform the exact same steps as Searching to locate the target key.
   2. If found, change the slot value to DELETED (Tombstone). Do not clear it to null.
   3. Decrement your item count ($n$).

## 7. Rehashing Logic
When the table gets too full (typically when $\alpha > 0.7$ for open addressing), operations degrade toward $O(n)$. The table must expand.
## The Process

   1. Allocate New Array: Create a brand new hash table array, usually double the size of the original (ideally chosen as the next closest prime number to minimize future modulo collisions).
   2. Re-calculate Indices: You cannot just copy the elements over directly into the same slots. Because $m$ (table size) changed, every single old key must be re-processed through the new hash function: $h_{new}(k) = k \pmod{m_{new}}$.
   3. Drop Tombstones: Any old DELETED markers are ignored during this process, naturally cleaning up the table memory.

------------------------------
## 8. Cheat Sheet Time Complexities

| Operation | Average Case | Worst Case | Reason for Worst Case |
|---|---|---|---|
| Insertion | $O(1)$ | $O(n)$ | High collision clusters / Table must resize |
| Deletion | $O(1)$ | $O(n)$ | High collisions / Searching a long chain or probe path |
| Searching | $O(1)$ | $O(n)$ | All items accidentally hashed to the exact same bucket |