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

---

## ⚠️ Common try-except Pitfall: Invalid `break` Outside a Loop

### ❌ Example That Raises a SyntaxError
```python
try:
    print(5 / 0)
    break  # 🚫 SyntaxError: 'break' outside loop
except:
    print("General error")
except (ValueError, ZeroDivisionError):
    print("Specific error")
```
---

## 🚨 Common Python Exceptions – Quick Reference

| Exception Name        | When It Happens (Trigger)                                       | Example                                 |
|-----------------------|------------------------------------------------------------------|------------------------------------------|
| `ValueError`          | Function gets the right type, but invalid value                 | `int("abc")`, `("a", "b").index("z")`    |
| `TypeError`           | Operation used with the wrong type                              | `len(5)`, `None * 3`                     |
| `SyntaxError`         | Code isn't valid Python syntax                                  | `print("Hi)`                             |
| `NameError`           | Variable is not defined                                         | `print(x)` when `x` isn't declared       |
| `IndexError`          | List or tuple index out of range                                | `[1, 2][5]`                              |
| `KeyError`            | Dictionary key not found                                        | `{"a": 1}["b"]`                          |
| `AttributeError`      | Attribute or method doesn't exist                               | `"hi".push()`                            |
| `ZeroDivisionError`   | Division or modulus by zero                                     | `5 / 0`, `10 // 0`                       |
| `ImportError`         | Can't import a module or object                                 | `from math import banana`               |
| `ModuleNotFoundError` | Specified module can't be found or installed                    | `import notamodule`                     |
| `IndentationError`    | Indentation rules violated (e.g., mixing tabs and spaces)       | Bad indent on `print()`                 |
| `RuntimeError`        | Generic error at runtime                                        | Often raised manually                   |
| `StopIteration`       | Iterator has no more items                                      | Using `next()` after loop ends          |
| `OverflowError`       | Result too large to represent (rare)                            | `math.exp(1000)`                         |

