# Chapter 10: Functions

## 1. What is a Function?
- A **function** is a reusable block of code that performs a specific task.
- Helps in organizing code, avoiding repetition.

---

## 2. Defining a Function

### Syntax:
```python
def function_name(parameters):
    # code block
    return value
```

### Example:
```python
def greet(name):
    return "Hello, " + name
```

---

## 3. Calling a Function

```python
message = greet("Alice")
print(message)  # Output: Hello, Alice
```

---

## 4. Parameters and Arguments

- **Parameters**: variables listed in function definition.
- **Arguments**: values passed when calling the function.

```python
def add(a, b):
    return a + b

print(add(2, 3))  # 5
```

---

## 5. Return Statement

- Ends function execution and sends back a value.
```python
def square(x):
    return x * x
```

---

## 6. Default Parameter Values

- Parameters can have default values.
```python
def greet(name="Guest"):
    print("Hello", name)
```

---

## 7. Keyword Arguments

- Call functions using `key=value`.
```python
def intro(name, age):
    print(name, age)

intro(age=25, name="Tom")
```

---

## 8. `None` as Default Return

- A function without a `return` returns `None`.

```python
def say_hi():
    print("Hi")

result = say_hi()
print(result)  # Output: None
```

---

## 9. Order of Parameters: Required vs Default

In Python, **non-default (required)** parameters must come **before** any **default** parameters in a function definition. If not, you'll get a `SyntaxError`.

This is because once Python starts assigning default values, it assumes all remaining parameters also have defaults.

### ❌ Invalid Example (will raise error):
```python
def add_numbers(a, b=2, c):
    print(a + b + c)

add_numbers(a=1, c=3)
```

**Error:**
```text
SyntaxError: non-default argument follows default argument
```

---

### ✅ Corrected Example:
```python
def add_numbers(a, c, b=2):
    print(a + b + c)

add_numbers(a=1, c=3)  # Output: 6
```

➡️ **Fix:** Move `c` (a required param) before `b=2` (a default param).

---

Functions help break large programs into smaller, manageable blocks.
