# ⏱️ Time Complexity — Complete Guide

Time Complexity defines **how an algorithm scales with input size (n)**.
It is the foundation of writing **efficient and interview-ready code**.

---

## 🚀 Why Time Complexity Matters

* ⚡ Helps choose the most efficient solution
* 📈 Predicts performance on large inputs
* 🎯 Essential for coding interviews and competitive programming

---

## 📊 Complexity Hierarchy (Best → Worst)

| Complexity | Name        | Example                 |
| ---------- | ----------- | ----------------------- |
| O(1)       | Constant    | Accessing array element |
| O(log n)   | Logarithmic | Binary Search           |
| O(n)       | Linear      | Single loop             |
| O(n log n) | Log-linear  | Merge Sort              |
| O(n²)      | Quadratic   | Nested loops            |
| O(2ⁿ)      | Exponential | Backtracking            |

---

## 🧠 Core Intuition

👉 Focus on **how many times your code runs as input grows**

* Small input → everything works
* Large input → only efficient code survives

---

## 🔍 How to Analyze Time Complexity

### 🔹 1. Single Loop → O(n)

```python
for i in range(n):
    pass
```

---

### 🔹 2. Nested Loops → O(n²)

```python
for i in range(n):
    for j in range(n):
        pass
```

---

### 🔹 3. Logarithmic Growth → O(log n)

```python
while n > 1:
    n //= 2
```

---

### 🔹 4. Independent Loops → O(n)

```python
for i in range(n):
    pass

for j in range(n):
    pass
```

---

### 🔹 5. Different Inputs → O(n + m)

```python
for i in range(n):
    pass

for j in range(m):
    pass
```

---

## ⚡ Golden Rules

* Ignore constants
  👉 O(2n) → O(n)

* Drop lower-order terms
  👉 O(n² + n) → O(n²)

* Always consider **worst-case complexity**

---

## 🧩 Common Patterns

| Pattern                | Complexity |
| ---------------------- | ---------- |
| Two nested loops       | O(n²)      |
| Halving input          | O(log n)   |
| Sorting-based problems | O(n log n) |

---

## ⚠️ Common Mistakes

### ❌ Assuming all nested loops are the same

```python
for i in range(n):
    for j in range(i):
        pass
```

✔ Still O(n²), but fewer operations

---

## 🧠 Interview Insight

On platforms like LeetCode:

* Brute force solutions → often fail on large inputs
* Optimized solutions → expected

👉 You’re judged not just on correctness, but efficiency.

---

## 🎯 What You Should Master

* Instantly recognize complexity
* Optimize O(n²) → O(n log n) or O(n)
* Clearly explain your approach

---

## 🔥 Practice Challenge

Find the complexity:

```python
for i in range(n):
    for j in range(i):
        print(i, j)
```

👉 Answer: **O(n²)**

---

## 💡 Final Thought

> Write code that not only works—but scales.
