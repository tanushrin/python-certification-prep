# Chapter 9: Lists and Basic Data Structures

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

## 3. Membership Testing
To check if item exists:
  ```python
  "apple" in fruits
  "kiwi" not in fruits
  ```

---

## 4. Slicing Lists

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

## 5. Modifying Lists

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
There are **three ways** to remove items from a list:

```python
fruits = ["apple", "banana", "cherry", "banana"]

# 1️⃣ Remove by value (first match)
fruits.remove("banana")      # Removes the first "banana"

# 2️⃣ Remove by index
del fruits[0]                # Removes "apple"

# 3️⃣ Remove the last item (or by index)
fruits.pop()                 # Removes the last item ("banana")
fruits.pop(0)                # Removes the first item (now "cherry")
```
  
### Reverse list:

The `reverse()` method **reverses the elements of a list in-place** — it does **not** return a new list.

#### 📌 Syntax:
```python
list.reverse()
```

#### ✅ Example:
```python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]
```

#### ⚠️ Important:
- It **modifies** the original list.
- If you need a **reversed copy** instead of modifying the original list, use slicing:
```python
reversed_list = numbers[::-1]
```

#### Summary:

| Method           | Action                      | Returns     |
|------------------|-----------------------------|-------------|
| `list.reverse()` | Reverses the list **in-place** | `None`      |
| `list[::-1]`     | Returns **reversed copy**     | New list    |

## 6. Copying a List Without Changing the Original

Sometimes you want to work with a **copy** of a list so that the original remains unchanged.

#### ✅ Ways to Copy a List:

| Method                  | Example                      | Notes                             |
|-------------------------|------------------------------|-----------------------------------|
| Slicing                | `copy = original[:]`         | Fast, commonly used               |
| `list()` constructor   | `copy = list(original)`      | Also creates a shallow copy       |
| `.copy()` method       | `copy = original.copy()`     | Preferred in Python 3.3+          |

#### Example:
```python
original = [1, 2, 3]
copy1 = original[:]           # Using slicing
copy2 = list(original)        # Using list constructor
copy3 = original.copy()       # Using .copy()

# Modify a copy
copy1.append(4)

print("Original:", original)  # [1, 2, 3]
print("Copy1:", copy1)        # [1, 2, 3, 4]
```

> 🔍 All the above create **shallow copies** — for nested lists, use `copy.deepcopy()`.

---

## 7. List Functions & Methods

A **method** is a **specific kind of function**. It behaves like a function and looks like one too, but differs in how it's invoked and what it operates on.

### 🔹 Function
- A function **doesn't belong to any data**.
- It receives data, processes it, and returns a result.
- Example:
  ```python
  result = len([1, 2, 3])  # function
  print(result)           # → 3

  numbers = [5, 2, 9]
  print(sorted(numbers))    # → [2, 5, 9]
  ```

### 🔹 Method
- A method is **owned by the data it works for**.
- It can **modify the internal state** of the object it belongs to.
- Invoked using **dot notation**.
- Example:
  ```python
  my_list = [3, 1, 2]
  my_list.sort()        # method
  print(my_list)        # → [1, 2, 3]
  ```

### 📌 Key Differences

| Feature        | Function                     | Method                         |
|----------------|------------------------------|--------------------------------|
| Ownership      | Belongs to global codebase   | Owned by object/data type      |
| Syntax         | `function(arg)`              | `data.method(arg)`             |
| Data Access    | Needs data as argument       | Operates on internal data      |
| State Changes  | Usually doesn't modify data  | Can modify the object itself   |

---

| Type        | Name             | Description                        |
|-------------|------------------|------------------------------------|
| **Function**| `len(list)`      | Returns number of elements         |
| **Function**| `sorted(list)`   | Returns a new sorted list          |
| **Method**  | `list.sort()`    | Sorts the list in place            |
| **Method**  | `list.append()`  | Adds an element to the end         |
| **Method**  | `list.insert()`  | Adds at specified index            |
| **Method**  | `list.remove()`  | Removes the specified element      |
| **Method**  | `list.pop()`     | Removes and returns last item (or by index) |
| **Method**  | `list.clear()`   | Empties the list                   |

---

### Example

```python
data = [4, 2, 7, 1]

print(len(data))        # → 4
print(sorted(data))     # → [1, 2, 4, 7]

data.sort()             # modifies original list
data.append(9)
data.remove(2)
print(data)             # → [1, 4, 7, 9]

data.pop()
print(data)             # → [1, 4, 7]

data.clear()
print(data)             # → []
```

---

> ✅ Remember: **methods change the object** they belong to, while **functions return new values**.
---

## 8. Nested Lists

Lists can contain other lists:
```python
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])  # 3
```
📌 [Explore Multi-Dimensional Lists (Nested Lists) →](Nested_Lists_Multidim.md)

---

Lists are one of Python’s most versatile and widely used data structures.
