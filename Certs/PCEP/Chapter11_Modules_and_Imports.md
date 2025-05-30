# 📦 Chapter 11: Modules and Imports

## 1. What is a Module?
- A **module** is a file containing Python code (usually functions, classes, variables).
- Helps in organizing and reusing code.

---

## 2. Importing a Module

### Basic Import:
```python
import math
print(math.sqrt(16))  # 4.0
```

### Import with Alias:
```python
import math as m
print(m.pi)
```

### Import Specific Items:
```python
from math import pi, sqrt
print(pi)
print(sqrt(9))
```

### Import All Items:
```python
from math import *
print(sin(0))
```

> ⚠️ Avoid `from module import *` in large programs — can cause name clashes.

---

## 3. Exploring Module Contents

### Use `dir()`:
```python
import math
print(dir(math))
```

### Use `help()`:
```python
help(math)
```

---

## 4. Creating Your Own Module

### Example:
**my_module.py**
```python
def greet(name):
    return "Hello " + name
```

**main.py**
```python
import my_module
print(my_module.greet("Alice"))
```

---

## 5. Built-in Modules

Common built-in modules:
- `math`: math functions
- `random`: generate random numbers
- `datetime`: date and time handling
- `os`: interacting with the operating system
- `sys`: system-specific parameters and functions

---

Using modules keeps your code clean, organized, and DRY (Don’t Repeat Yourself).