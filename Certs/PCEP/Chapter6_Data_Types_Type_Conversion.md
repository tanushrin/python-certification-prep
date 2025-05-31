# 🧠 Chapter 6: Data Types and Type Conversion

## 1. Built-in Data Types

### Numeric Types
- `int`: Integer numbers  
  Example: `10`, `-3`, `0x1F`
- `float`: Decimal numbers  
  Example: `3.14`, `-0.5`, `1e-2`, `4.`, `3E8`

  ```python
  # exponent (value after e) must be an integer
  x = 3e4     # valid
  x = 1.2E-2  # valid
  x = 1e2.5   # ❌ invalid – exponent must be an integer
  ```

💡 The part **after `e` must always be an integer**, even if the base is a float.

  
- `complex`: Complex numbers  
  Example: `3+4j`

### Sequence Types
- `str`: Strings (text)  
  Example: `"hello"`, `'123'`, ```python   "I like \"Monty Python\""  ```

### Other Types
- `bool`: Boolean values (`True`, `False`)
- `NoneType`: Represents "no value" (`None`)

---

## 2. Type Checking

Use the `type()` function to check the type of a variable:

```python
x = 5
print(type(x))  # <class 'int'>
```

---

## 3. Type Conversion (Type Casting)

Convert between data types using built-in functions:

### Common Conversions:
```python
int("10")      # 10
float("3.14")  # 3.14
str(123)       # '123'
bool(0)        # False
```

### Conversion Table:
| From   | To        | Example        | Result  |
|--------|-----------|----------------|---------|
| str    | int       | `int("42")`    | 42      |
| str    | float     | `float("2.5")` | 2.5     |
| int    | str       | `str(100)`     | "100"   |
| int    | float     | `float(5)`     | 5.0     |
| float  | int       | `int(3.9)`     | 3       |
| any    | bool      | `bool("")`     | False   |

---

## 4. Truthy and Falsy Values


| Value        | Boolean Equivalent | Note                               |
|--------------|--------------------|------------------------------------|
| `None`       | `False`            | Behaves like False in conditions, but `None != False` |
| `0`, `0.0`   | `False`            | Zero is always falsy               |
| `""`, `[]`   | `False`            | Empty string/list is falsy         |
| Non-zero or non-empty | `True`   | Anything with content is truthy    |


---

## 5. Errors in Conversion

- Trying to convert invalid strings to numbers raises `ValueError`:

```python
int("abc")  # ValueError
```

---

Note: Python automatically infers types, but conversion is useful for compatibility or input handling.
