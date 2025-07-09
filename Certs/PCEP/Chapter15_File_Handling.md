# 📘 Chapter 13: File Handling

## 1. Opening Files

### Syntax:
```python
file = open("filename.txt", "mode")
```

### Common Modes:
| Mode | Description              |
|------|--------------------------|
| `'r'` | Read (default)          |
| `'w'` | Write (overwrite)       |
| `'a'` | Append (end of file)    |
| `'b'` | Binary mode             |
| `'+'` | Read and write          |

---

## 2. Reading Files

### `.read()`
Reads entire file:
```python
file = open("example.txt", "r")
content = file.read()
file.close()
```

### `.readline()`
Reads one line at a time:
```python
line = file.readline()
```

### `.readlines()`
Reads all lines into a list:
```python
lines = file.readlines()
```

---

## 3. Writing to Files

### `.write()`
Writes a string to a file:
```python
file = open("output.txt", "w")
file.write("Hello World")
file.close()
```

> ⚠️ `write()` does NOT add a newline automatically.

---

## 4. `with` Statement (Best Practice)

Automatically closes file:
```python
with open("data.txt", "r") as file:
    data = file.read()
```

---

## 5. File Object Methods

| Method      | Description                    |
|-------------|--------------------------------|
| `read()`    | Reads entire file              |
| `readline()`| Reads next line                |
| `readlines()`| Reads all lines to list       |
| `write()`   | Writes a string                |
| `close()`   | Closes the file                |

---

Proper file handling ensures data persistence and avoids resource leaks.
