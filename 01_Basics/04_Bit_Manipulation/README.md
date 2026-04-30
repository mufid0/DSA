# ⚙️ Bit Manipulation

Bit Manipulation involves performing operations directly on the **binary representation of numbers**.
It is one of the most powerful techniques for writing **efficient and optimized algorithms**.

---

## 📂 Contents

* `basics.py` → Fundamental bit operations (AND, OR, XOR, shifts, bit checks)
* `count_set_bits.py` → Counting number of 1s in binary (multiple approaches)

---

## 🚀 Why Bit Manipulation Matters

* ⚡ Extremely fast operations (constant time)
* 📉 Reduces time and space complexity
* 🎯 Frequently asked in coding interviews

---

## 📌 Core Concepts

### 🔹 Bitwise Operators

| Operator | Symbol | Description                    |
| -------- | ------ | ------------------------------ |
| AND      | `&`    | Sets bit if both bits are 1    |
| OR       | `\|`   | Sets bit if at least one is 1  |
| XOR      | `^`    | Sets bit if bits are different |
| NOT      | `~`    | Inverts bits                   |

---

### 🔹 Shift Operators

| Operator | Description                |
| -------- | -------------------------- |
| `<<`     | Left shift (multiply by 2) |
| `>>`     | Right shift (divide by 2)  |

---

## 🧠 Common Operations

* Check even/odd
* Get k-th bit
* Set / clear / toggle bits
* Count set bits

---

## 🔢 Counting Set Bits

### Approaches Implemented

1. **Basic Method**

   * Check each bit
   * Time: O(log n)

2. **Brian Kernighan’s Algorithm**

   * Removes lowest set bit
   * Time: O(number of set bits)

3. **Python Built-in**

   * `bin(n).count('1')`
   * Fast and simple

---

## ⚡ Complexity

| Operation             | Time                |
| --------------------- | ------------------- |
| Basic bit operations  | O(1)                |
| Count set bits        | O(log n)            |
| Kernighan’s algorithm | O(k) (k = set bits) |

---

## 🧩 When to Use

* Optimization problems
* Subset generation
* XOR-based problems
* Low-level performance tuning

---

## ⚠️ Common Mistakes

* ❌ Confusing bit positions (0-indexed vs 1-indexed)
* ❌ Not understanding binary representation
* ❌ Overusing built-ins without understanding logic

---

## 🎯 Learning Outcome

After this section, you will:

* Understand bitwise operations clearly
* Apply bit tricks in problem solving
* Write optimized and efficient code

---

## 🔥 Practice Ideas

* Check if a number is a power of 2
* Find the single non-repeating element
* Generate all subsets using bits

---

## 💡 Pro Tip

Bit manipulation often turns:

* ❌ O(n) → O(1)
* ❌ Complex logic → simple operations

---

> “Master bits, and you master optimization.”
