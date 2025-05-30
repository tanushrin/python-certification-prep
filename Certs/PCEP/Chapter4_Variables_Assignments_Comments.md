# 💬 Chapter 4: Variables, Assignments & Comments

## 1. What is a Variable?
- A **variable** is a named container to store data.
- It references a value stored in memory.

---

## 2. Naming Rules
- Must begin with a **letter** or **underscore** (`_`)
- Can contain **letters**, **digits**, and **underscores**
- Cannot start with a digit
- Cannot use **Python keywords** (e.g., `if`, `class`, `return`)

### ✅ Valid:
```python
my_var = 10
_var1 = 'hello'
```

### ❌ Invalid:
```python
2cool = 5     # starts with digit
class = 'bad' # keyword
```

---

## 3. Assigning Values
- Use `=` to assign a value
```python
x = 5
name = "Alice"
```

- You can assign same value to multiple variables:
```python
a = b = c = 10
```

- Or assign multiple values at once:
```python
x, y = 1, 2
```

---

## 4. Dynamic Typing
- Python is **dynamically typed**: variable types can change
```python
x = 5
x = "Now I'm a string!"
```

---

## 5. Comments
- **Single-line**: use `#`
```python
# This is a comment
x = 5  # Inline comment
```

- **Multi-line** (not official syntax): use triple quotes
```python
'''
This is a 
multi-line comment
'''
```

---

## 6. Compound Assignment Operators
| Operator | Meaning                | Example       |
|----------|------------------------|---------------|
| `+=`     | Add & assign           | `x += 1`      |
| `-=`     | Subtract & assign      | `x -= 1`      |
| `*=`     | Multiply & assign      | `x *= 2`      |
| `/=`     | Divide & assign        | `x /= 2`      |
| `//=`    | Floor divide & assign  | `x //= 2`     |
| `%=`     | Modulo & assign        | `x %= 2`      |
| `**=`    | Power & assign         | `x **= 3`     |

Note: Python variables don’t need declarations. They are created the moment you assign a value.