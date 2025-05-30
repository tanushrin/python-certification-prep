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