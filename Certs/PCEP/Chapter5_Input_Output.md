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

### 🛠️ Customizing Output in `print()`

- `sep`: defines the **separator** between multiple values  
  *(default is a space — i.e., `sep=' '`)*
- `end`: defines **what is printed at the end** of the line  
  *(default is a newline — i.e., `end='\n'`)*


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


## 🕓 Mini Project: Calculating End Time of an Event

This small program asks the user for a starting time (in hours and minutes) and a duration (in minutes), then calculates the end time in **24-hour format**.

### 🔤 Code:

```python
# Ask for user input
start_hour = int(input("Enter starting hour (0–23): "))
start_minute = int(input("Enter starting minute (0–59): "))
duration = int(input("Enter duration in minutes: "))

# Convert to total minutes and add duration
start_total_mins = start_hour * 60 + start_minute
end_total_mins = start_total_mins + duration

# Convert back to hours and minutes (24-hour format)
end_hour = (end_total_mins // 60) % 24
end_minute = end_total_mins % 60

# Display result
print(f"New time: {end_hour:02d}:{end_minute:02d}")
```
### Example:

```python
Enter starting hour (0–23): 12
Enter starting minute (0–59): 17
Enter duration in minutes: 59
New time: 13:16
```
