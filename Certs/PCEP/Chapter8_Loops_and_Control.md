# 🔁 Chapter 8: Loops and Control Statements

## 1. The `while` Loop

### Syntax:
```python
while condition:
    # block of code
```

### Example:
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

- Runs as long as the condition is `True`.
- Risk of infinite loop if the condition never becomes `False`.

```python
# Loop with while and else
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

# Output:
# 1
# 2
# 3
# 4
# else: 5
```

```python
# If the condition is False initially, only the else block runs
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

# Output:
# else: 5
```
The else block in loops:
- Runs only <b>after the loop finishes normally (not via</b> break)
- Executes <b>even if the loop body doesn’t run at all</b>

---

## 2. The `for` Loop

### Syntax:
```python
for variable in iterable:
    # block of code
```

### Example:
```python
for i in range(3):
    print("Hello")
```

### The `range()` Function:
- `range(stop)`
- `range(start, stop)`
- `range(start, stop, step)`

### Example:
```python
for i in range(1, 6, 2):  # 1, 3, 5
    print(i)
```

---

## 3. Loop Control Statements

### `break`
- Exits the loop immediately.
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### `continue`
- Skips the rest of the current loop and continues with the next iteration.
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

### `pass`
- Placeholder statement; does nothing.
```python
if True:
    pass  # to be implemented later
```

---

## 4. Nested Loops

### Example:
```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

---

Loops let you repeat tasks efficiently. Combine with conditions and ranges for flexible control.


---

## 5. Examples Loop Control Statements
```python


# --- break ---
# Exits the loop immediately when i == 5
for i in range(10):
    if i == 5:
        break
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# --- continue ---
# Skips printing 2; goes to next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)

# Output:
# 0
# 1
# 3
# 4

# --- pass ---
# Placeholder in control structures
if True:
    pass  # Does nothing here, useful during development
```

```python
# Ask user for a word and convert to uppercase
user_word = input("Enter a word: ")
user_word = user_word.upper()

# Loop through each letter and skip vowels
for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)

# Sample Inputs and Expected Outputs:

# Input: Gregory
# Output:
# G
# R
# G
# R
# Y

# Input: abstemious
# Output:
# B
# S
# T
# M
# S

# Input: IOUEA
# Output: (prints nothing)
```

### Pyramid Height Calculator

This program calculates how many **complete levels** of a pyramid can be built using a given number of blocks. Each level uses one more block than the previous.

```python
# Ask user for number of blocks
blocks = int(input("Enter number of blocks: "))

# Initialize height of pyramid and blocks needed for the current level
height = 0
needed = 1

# Keep building levels as long as we have enough blocks
while needed <= blocks:
    blocks -= needed     # Use blocks for the current level
    height += 1          # Increase pyramid height
    needed += 1          # Next level needs one more block

# Display the final height
print("The height of the pyramid:", height)
```

#### Example:
Input: `6`  
Output: `The height of the pyramid: 3`

---
📌 **Logic**:
- Level 1 needs 1 block  
- Level 2 needs 2 blocks  
- Level 3 needs 3 blocks  
- You can build as many levels as long as total blocks are enough.

---

### Collatz Conjecture (Mini Project)

In 1937, mathematician Lothar Collatz proposed a hypothesis (still unproven) that:

> For any non-zero positive integer `c0`, repeatedly apply the following rules:
> - If `c0` is even: `c0 = c0 // 2`
> - If `c0` is odd: `c0 = 3 * c0 + 1`
> 
> Eventually, the sequence will always reach 1.

#### Your Task:
- Read a positive integer from the user.
- Print each value of `c0` in the sequence.
- Count and display how many steps it takes to reach 1.

```python
c0 = int(input("Enter a positive number: "))
steps = 0

while c0 != 1:
    print(c0)
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    steps += 1

print(1)
print("steps =", steps)
```

#### Sample Input:
```
15
```

#### Expected Output:
```
15
46
23
70
35
106
53
160
80
40
20
10
5
16
8
4
2
1
steps = 17
```


