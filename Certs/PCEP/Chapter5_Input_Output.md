# 📤 Chapter 5: Basic Input and Output in Python

## 1. `input()` Function
- Used to get input from the user.
- Always returns a **string**.

### Syntax:
```python
name = input("Enter your name: ")
```

### Example:
```python
age = input("Enter age: ")
print("You entered:", age)
```

### Important:
- Convert input to other types using:
```python
int(input("Enter a number: "))
float(input("Enter a decimal: "))
```
- If conversion fails, Python raises `ValueError`.

---

## 2. `print()` Function
- Displays output on the console.
- Can print multiple values, separated by commas.

### Syntax:
```python
print("Hello", "World")
```

### Customizing Output
- `sep`: defines separator between values
- `end`: defines what is printed at the end (default is newline)

### Examples:
```python
print("A", "B", sep="-")       # A-B
print("Line 1", end="...")     # Line 1...
print("Next")                  # ...Next
```

---

## 3. Escape Sequences
Used in strings to represent special characters:
| Escape | Meaning         |
|--------|-----------------|
| `\n`  | Newline         |
| `\t`  | Tab             |
| `\\` | Backslash       |
| `\'`  | Single quote    |
| `\"`  | Double quote    |

### Example:
```python
print("Hello\nWorld")  # Hello
                        # World
```

---

> Tip: `input()` is for interaction, `print()` is for feedback. Together, they make your scripts user-friendly.