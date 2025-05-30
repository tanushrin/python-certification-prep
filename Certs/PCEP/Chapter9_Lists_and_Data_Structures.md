# 🧺 Chapter 9: Lists and Basic Data Structures

## 1. What is a List?
- A **list** is a collection of ordered, changeable (mutable) items.
- Defined using square brackets `[]`.

### Example:
```python
fruits = ["apple", "banana", "cherry"]
```

---

## 2. Accessing List Elements

- Indexing starts from 0.
```python
print(fruits[0])  # "apple"
```

- Negative indices access from end:
```python
print(fruits[-1])  # "cherry"
```

---

## 3. Slicing Lists

### Syntax:
```python
list[start:stop:step]
```

### Example:
```python
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])      # [1, 2, 3]
print(numbers[:3])       # [0, 1, 2]
print(numbers[::2])      # [0, 2, 4]
```

---

## 4. Modifying Lists

### Update an item:
```python
fruits[1] = "blueberry"
```

### Add items:
```python
fruits.append("date")        # Add to end
fruits.insert(1, "kiwi")     # Add at index 1
```

### Remove items:
```python
fruits.remove("banana")      # Remove by value
fruits.pop()                 # Remove last item
```

---

## 5. List Functions & Methods

| Function       | Description                        |
|----------------|------------------------------------|
| `len(list)`    | Length of list                     |
| `sorted(list)` | Returns a new sorted list          |
| `list.sort()`  | Sorts the list in place            |
| `list.append()`| Adds an element to the end         |
| `list.insert()`| Adds at specified position         |
| `list.remove()`| Removes specified element          |
| `list.pop()`   | Removes element at given position  |
| `list.clear()` | Removes all elements               |

---

## 6. Nested Lists

Lists can contain other lists:
```python
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])  # 3
```

---

Lists are one of Python’s most versatile and widely used data structures.