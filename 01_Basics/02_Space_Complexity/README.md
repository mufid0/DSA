# 📦 Space Complexity — Complete Guide

Space Complexity measures **how much memory an algorithm uses as input size (n) grows**.

It includes:

* Input space
* Auxiliary (extra) space

---

## 🚀 Why Space Complexity Matters

* ⚡ Helps optimize memory usage
* 📱 Critical for large-scale systems
* 🎯 Often required in coding interviews

---

## 🧠 Key Concept

👉 Focus on **extra memory used**, not just input size

---

## 📊 Types of Space Complexity

### 🔹 1. Constant Space — O(1)

Uses fixed memory regardless of input size.

```python
def sum_array(arr):
    total = 0
    for x in arr:
        total += x
    return total
```

✔ Only one variable used → O(1)

---

### 🔹 2. Linear Space — O(n)

Memory grows with input size.

```python
def copy_array(arr):
    return [x for x in arr]
```

✔ New array created → O(n)

---

### 🔹 3. Logarithmic Space — O(log n)

Used in recursive calls or divide-and-conquer.

```python
def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)
```

✔ Recursive stack depth → O(log n)

---

## ⚡ Auxiliary Space vs Total Space

| Type            | Meaning              |
| --------------- | -------------------- |
| Input Space     | Memory used by input |
| Auxiliary Space | Extra memory used    |

👉 In interviews, focus on **auxiliary space**

---

## 🧩 Common Patterns

| Pattern         | Space    |
| --------------- | -------- |
| Variables only  | O(1)     |
| New array/list  | O(n)     |
| Recursion stack | O(depth) |

---

## ⚠️ Common Mistakes

### ❌ Ignoring recursion stack

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

👉 Space Complexity = O(n), not O(1)

---

### ❌ Confusing input space with extra space

```python
arr = [1, 2, 3]
```

👉 Input space ≠ auxiliary space

---

## 🧠 Interview Insight

On platforms like LeetCode:

* You may be asked to:

  * Optimize time **AND** space
  * Convert O(n) space → O(1)

---

## 🎯 What You Should Master

* Identify auxiliary space quickly
* Optimize memory usage
* Understand recursion space cost

---

## 🔥 Practice Challenge

Find space complexity:

```python
def func(n):
    if n == 0:
        return
    func(n - 1)
```

👉 Answer: **O(n)** (recursive stack)

---

## 💡 Final Thought

> Efficient code is not just fast—it’s memory aware.


