# 🧮 Chapter 2: Python Basic Types and Literals

## 1. What is a Literal?
- A **literal** is a fixed value directly represented in code.
- Its format determines its **type** (e.g., `123` is `int`, `1.23` is `float`, `'abc'` is `string`).

---

## 2. Integer Literals
- Whole numbers, no decimal point.
- Can include underscores for readability: `1_000_000`
- Can be:
  - **Decimal**: `123`
  - **Binary**: `0b1010`
  - **Octal**: `0o77`
  - **Hexadecimal**: `0x1A`

### Examples:
```python
111     # valid
+1      # positive
-3      # negative
0x11    # hexadecimal (17)
0b111   # binary (7)
```

---

## 3. Floating Point Literals (`float`)
- Contain a dot `.` or exponent notation `e`.
- Use scientific notation: `1.5e2` → `150.0`

### Examples:
```python
1.1
.1
1.
1.1e-2
-1.1E2
```

---

## 4. String Literals
- Enclosed in single or double quotes
- Multi-line strings use triple quotes
- Escape characters:
  - `\` backslash
  - `'` apostrophe
  - `"` quote
  - `\n` newline
  - `\t` tab

### Examples:
```python
"Hello"
'Python\'s den'
"""Multi
Line"""
```

---

## 5. Boolean Literals
- Only two: `True`, `False`

---

## 6. None Literal
- `None` represents the absence of a value

> 🧠 Tip: Knowing literals is crucial for understanding what kind of data your variables are storing.