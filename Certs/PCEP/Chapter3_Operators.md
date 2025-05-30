# ➗ Chapter 3: Operators

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

---

### ➖ Unary Operators
| Operator | Description        | Example |
|----------|--------------------|---------|
| `-`      | Negation           | `-2` → `-2` |
| `+`      | Identity (unchanged)| `+2` → `2` |

---

## 3. Operator Precedence (High → Low)
1. `**` (Right-to-left binding)
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