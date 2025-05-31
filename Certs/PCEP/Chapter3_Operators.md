# Chapter 3: Operators

## 1. What is an Operator?
- An **operator** performs an operation on one or more operands.
- Operands are the values or variables operators act upon.

---

## 2. Types of Operators in Python

### 🔢 Arithmetic Operators
| Operator | Name            | Example  | Result |
|----------|-----------------|----------|--------|
| `+`      | Addition        | 2 + 3    | 5      |
| `-`      | Subtraction     | 5 - 2    | 3      |
| `*`      | Multiplication  | 2 * 3    | 6      |
| `/`      | Division        | 4 / 2    | 2.0 (float) |
| `//`     | Integer Division| 5 // 2   | 2      |
| `%`      | Modulus         | 5 % 2    | 1      |
| `**`     | Exponentiation  | 2 ** 3   | 8      |

🧠 **Division** always returns a float  
💥 Division by zero raises `ZeroDivisionError`

### Integer Division (`//`) and Rounding Behavior

```python
# Integer by integer division gives an integer result:
print(6 // 4)    # 6 divided by 4 = 1.5 → floored to 1 (int)
print(6. // 4)   # 6.0 divided by 4 = 1.5 → floored to 1.0 (float)

# Now try with negative values:
print(-6 // 4)   # -6 / 4 = -1.5 → floored to -2
print(6. // -4)  # 6.0 / -4 = -1.5 → floored to -2.0
```

---

### ➖ Unary Operators
| Operator | Description        | Example |
|----------|--------------------|---------|
| `-`      | Negation           | `-2` → `-2` |
| `+`      | Identity (unchanged)| `+2` → `2` |

---

## 3. Operator Precedence (High → Low)
1. `**` (Right-to-left binding)

    Ex: `2 ** 3 ** 2 → 2 ** 9 = 512`  ✅

2. `*`, `/`, `//`, `%`
3. `+`, `-`

🧭 Use parentheses `()` to change evaluation order.

---

## 4. String Operators
| Operator | Name          | Example      | Result     |
|----------|---------------|--------------|------------|
| `+`      | Concatenation | `'a' + 'b'`  | `'ab'`     |
| `*`      | Replication   | `'a' * 3`    | `'aaa'`    |

---

## 5. Boolean Operators (Requires Boolean values)
| Priority | Operator | Name        | Example            | Result |
|----------|----------|-------------|---------------------|--------|
| High     | `not`    | Negation    | `not False`         | True   |
| Medium   | `and`    | Conjunction | `True and False`    | False  |
| Low      | `or`     | Disjunction | `True or False`     | True   |

---

## 6. Relational (Comparison) Operators
| Operator | Name            | Example   | Result |
|----------|------------------|-----------|--------|
| `==`     | Equal to         | 2 == 2    | True   |
| `!=`     | Not equal to     | 2 != 3    | True   |
| `>`      | Greater than     | 3 > 2     | True   |
| `<`      | Less than        | 1 < 2     | True   |
| `>=`     | Greater or equal | 2 >= 2    | True   |
| `<=`     | Less or equal    | 1 <= 2    | True   |

---

> ⚙️ Operators follow **left-sided binding** (except `**` which is right-sided).
> Use parentheses `()` to clarify or override order of operations.

---

## 7. Compound Assignment Operators

Python allows us to simplify expressions like:

```python
# General format:
variable = variable op expression

# Can be rewritten as:
variable op = expression

# Examples:
i = i + 2 * j                 # ➝ i += 2 * j
var = var / 2                 # ➝ var /= 2
rem = rem % 10                # ➝ rem %= 10
j = j - (i + var + rem)       # ➝ j -= (i + var + rem)
x = x ** 2                    # ➝ x **= 2
```

### Expression Evaluation Example (Operator Precedence)

Which of the following expressions evaluate to a **non-zero** result?  
(**Select two answers.**)

| Expression             | Evaluation                          | Result  | ✅ Non-Zero? |
|------------------------|--------------------------------------|---------|--------------|
| `4 / 2 + 2 ** 1`       | `2.0 + 2`                            | `4.0`   | ✅ Yes        |
| `1 // 2 + 3 * 4`       | `0 + 12`                             | `12`    | ✅ Yes        |
| `1 ** 2 - 4 // 3`      | `1 - 1`                              | `0`     | ❌ No         |
| `4 / 2 - 2 ** 1`       | `2.0 - 2`                            | `0.0`   | ❌ No         |
| `1 - 2 // 3 + 4`       | `1 - 0 + 4`                          | `5`     | ✅ Yes        |
| `10 % 4 % 3`           | `(10 % 4) % 3 = 2 % 3`               | `2`     | ✅ Yes        |

---

📌 **Key Notes:**
- `**` has the highest precedence (evaluated right-to-left).
- when at least one `**` argument is a float, the result is a float, too.
- `/` always returns a `float`.
- `//` performs floor division (result is integer).
- `%` (modulo) uses left-to-right (left-sided) binding just like `+, -, *, //`.

