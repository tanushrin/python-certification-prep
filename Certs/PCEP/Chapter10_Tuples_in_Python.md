# 📘 Chapter 10: Tuples in Python

## 1. What is a Tuple?
- A **tuple** is a collection of **ordered**, **unchangeable (immutable)** items.
- Defined using **parentheses** `()` instead of square brackets.

### Example:
```python
tuple1 = (1, 2, 3)
print(tuple1)       # (1, 2, 3)
print(type(tuple1)) # <class 'tuple'>
```

---

## 2. Creating Tuples
- With multiple items:
```python
colors = ("red", "green", "blue")
```

- With one item (**singleton tuple**):
```python
one_item = (5,)  # comma is required!
```

- Without parentheses (works, but not recommended):
```python
nums = 1, 2, 3
```

---

## 3. Accessing Elements
- Indexing and slicing works the same as with lists:
```python
my_tuple = (10, 20, 30, 40)
print(my_tuple[1])     # 20
print(my_tuple[-1])    # 40
print(my_tuple[1:3])   # (20, 30)
```

---

## 4. Immutability of Tuples
- Tuples **cannot be changed** after creation:
```python
my_tuple = (1, 2, 3)
my_tuple[0] = 5      # ❌ TypeError
```

---

## 5. Tuple Functions and Methods
| Function / Method   | Description                        |
|---------------------|------------------------------------|
| `len(tuple)`        | Returns number of elements         |
| `tuple.count(x)`    | Counts occurrences of value `x`    |
| `tuple.index(x)`    | Returns index of first occurrence  |

### Example:
```python
t = (1, 2, 2, 3)
print(len(t))        # 4
print(t.count(2))    # 2
print(t.index(3))    # 3
```

---

## 6. Tuple Packing and Unpacking
- Packing: grouping values into a tuple
```python
packed = 10, 20, 30
```

- Unpacking:
```python
a, b, c = packed
print(a, b, c)    # 10 20 30
```

---

## 7. When to Use Tuples
- Use **tuples** when:
  - You want a **fixed collection** of values.
  - The data should **not be modified**.
  - For **faster** access compared to lists.
  - You want to use the collection as a **dictionary key**.

> ✅ Tuples are safer and more efficient for storing constant data.

---

## 8. Nested Tuples
Tuples can contain other tuples or lists:
```python
data = ((1, 2), (3, 4))
print(data[1][0])   # 3
```

---

## 9. Converting Between Tuples and Lists
```python
lst = [1, 2, 3]
tpl = tuple(lst)
print(tpl)   # (1, 2, 3)

new_list = list(tpl)
print(new_list)  # [1, 2, 3]
```

---

---

## 10. Tuple Concatenation

You can **concatenate tuples** using the `+` operator. This creates a new tuple by joining the elements of both tuples.

```python
tup = (1,) + (1,)
print(tup)           # Output: (1, 1)
print(len(tup))      # Output: 2
```

### ⚠️ Important:
- Make sure to include the comma in single-element tuples: `(1,)`, not `(1)`  
  `(1)` is just an integer, not a tuple!

```python
print(type((1)))   # <class 'int'>
print(type((1,)))  # <class 'tuple'>
```

```python
tup = (1,)
tup = tup + tup     # (1,) + (1,) → (1, 1)
tup = tup + tup     # (1, 1) + (1, 1) → (1, 1, 1, 1)
print(tup)          # Output: (1, 1, 1, 1)
print(len(tup))     # Output: 4
```

Tuples are **immutable**, so each `+` operation returns a **new tuple**.

---


> 📌 Tuples are immutable, ordered, and support indexing just like lists — but they cannot be changed after creation.
