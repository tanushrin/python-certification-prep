# 📘 Chapter 11: Dictionaries in Python

## 1. What is a Dictionary?

- A **dictionary** is a mutable, unordered collection of key–value pairs.
- Defined using curly braces `{}`.

### ✅ Example:
```python
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "Zurich"
}
```

---

## 2. Accessing Values

- You can access values using their **keys**:
```python
print(my_dict["name"])       # Alice
```

- Or use the `.get()` method to avoid `KeyError`:
```python
print(my_dict.get("age"))    # 30
print(my_dict.get("salary")) # None (doesn't crash)
```

---

## 3. Modifying Values

- Assign a new value to an existing key:
```python
my_dict["city"] = "Geneva"
```

---

## 4. Adding and Removing Items

### Add:
```python
my_dict["email"] = "alice@example.com"
```

### Remove:
```python
del my_dict["age"]              # removes key 'age'
my_dict.pop("city")             # removes and returns the value
```

### Remove all:
```python
my_dict.clear()
```

---

## 5. Dictionary Length
```python
print(len(my_dict))  # Number of key–value pairs
```

---

## 6. Looping Through a Dictionary

### 🔄 Keys and Values:
```python
for key, value in my_dict.items():
    print(key, "→", value)
```

### 🔄 Just Keys:
```python
for key in my_dict:
    print(key)
```

### 🔄 Just Values:
```python
for value in my_dict.values():
    print(value)
```

---

## 7. Checking Membership

```python
if "name" in my_dict:
    print("Yes!")
```

---

## 8. Copying a Dictionary

```python
copy_dict = my_dict.copy()
```

---

## 9. Updating a Dictionary

You can merge or update values using `.update()`:
```python
my_dict.update({"age": 35, "city": "Basel"})
```

---

## 🧪 Mini Exercise

```python
phonebook = {}  # create empty dictionary
phonebook["Adam"] = 3456783456
phonebook["Eve"] = 9876543210
print(phonebook)

del phonebook["Adam"]
print(phonebook)
```

---

> ✅ A dictionary key must be **immutable** (e.g., strings, numbers, tuples) and **unique** within a dictionary.

