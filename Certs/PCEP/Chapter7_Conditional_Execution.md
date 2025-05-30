# 🔁 Chapter 7: Conditional Execution

## 1. The `if` Statement

### Basic Syntax:
```python
if condition:
    # block of code
```

### Example:
```python
x = 10
if x > 5:
    print("x is greater than 5")
```

---

## 2. The `if-else` Statement

### Syntax:
```python
if condition:
    # if block
else:
    # else block
```

### Example:
```python
age = 17
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## 3. The `if-elif-else` Chain

### Syntax:
```python
if condition1:
    # block 1
elif condition2:
    # block 2
else:
    # default block
```

### Example:
```python
score = 75
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
else:
    print("C")
```

---

## 4. Indentation Matters!
- Python uses **indentation** (usually 4 spaces) to define blocks.
- Misaligned code raises `IndentationError`.

---

## 5. Nested Conditions

### Example:
```python
x = 10
if x > 0:
    if x % 2 == 0:
        print("Positive even number")
```

---

## 6. Logical Conditions

- Combine conditions using:
  - `and` → True if both are true
  - `or` → True if at least one is true
  - `not` → Inverts a condition

### Example:
```python
age = 20
is_student = True
if age < 25 and is_student:
    print("Eligible for discount")
```

---

Use conditionals to control which parts of your program run based on data and logic.