# 📘 Multi-Dimensional Lists in Python (Nested Lists)

While Python doesn’t have built-in support for true multi-dimensional arrays like some other languages, you can simulate them using **nested lists**.

---

## 📌 What is a Nested List?

A **nested list** is simply a list that contains other lists as its elements.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Here, `matrix` acts like a 3×3 grid (or a 2D array).

---

## 🎯 Accessing Elements

To access an element, use two index values:

```python
print(matrix[0][1])  # → 2 (Row 0, Column 1)
print(matrix[2][2])  # → 9 (Row 2, Column 2)
```

---

## 🔁 Looping through a 2D List

### Row-wise traversal:
```python
for row in matrix:
    print(row)
```

### Access each item individually:
```python
for row in matrix:
    for item in row:
        print(item, end=" ")
```

---

## Note on Dimensions

- A list like `[ [1, 2], [3, 4] ]` is **2D**.
- You can nest lists within lists to simulate **3D** and higher dimensions.

```python
cube = [
    [[1], [2]],
    [[3], [4]]
]
print(cube[1][0][0])  # → 3
```

---

## Why Not Use Real Arrays?

Python’s built-in lists are flexible, but if you need **real multi-dimensional arrays**, use external libraries like **NumPy**:

```python
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[1][2])  # → 6
```

> 🚫 NumPy is not covered in PCEP.

---

## ✅ Summary
| Feature              | Built-in Lists | NumPy Arrays |
|----------------------|----------------|--------------|
| Nested Dimensions    | ✅ Yes         | ✅ Yes       |
| Fixed Data Types     | ❌ No          | ✅ Yes       |
| Used in PCEP         | ✅ Yes         | ❌ No        |

Use **nested lists** to simulate simple 2D or 3D structures in PCEP preparation.
