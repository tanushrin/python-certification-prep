# 🐞 Chapter 12: Errors and Exceptions

## 1. What is an Exception?
- An **exception** is an error that occurs during program execution.
- If not handled, it crashes the program.

---

## 2. Common Exceptions

| Exception        | Cause                            |
|------------------|----------------------------------|
| `ZeroDivisionError` | Division by zero            |
| `ValueError`     | Invalid value (e.g., int("abc")) |
| `TypeError`      | Wrong data type used            |
| `NameError`      | Using undefined variable        |
| `IndexError`     | List index out of range         |
| `KeyError`       | Dictionary key not found        |

---

## 3. Using `try-except`

### Syntax:
```python
try:
    # code that may cause error
except ErrorType:
    # code to handle error
```

### Example:
```python
try:
    x = int("abc")
except ValueError:
    print("Invalid conversion!")
```

---

## 4. `try-except-else-finally`

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Division error")
else:
    print("No error occurred")
finally:
    print("This block always runs")
```

- `else`: runs if no exception occurs.
- `finally`: always runs — use for cleanup.

---

## 5. Raising Exceptions Manually

```python
raise ValueError("Invalid value")
```

---

Handling exceptions makes programs robust and user-friendly.
