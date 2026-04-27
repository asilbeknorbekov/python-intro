# 🐍 Python Fundamentals — Core Concepts & Practice

A collection of Python scripts covering core programming concepts, written while learning the language from scratch. Each file focuses on a specific topic and is intended to be readable as a study reference as well as runnable code.

---

## Files

| File | What it covers |
|---|---|
| `Compare while and for loop.py` | Side-by-side loop implementations to understand control flow |
| `Decimal to Binary.py` | Converting numbers from base-10 to binary using modular arithmetic |
| `fibonacci.py` | Fibonacci sequence — iterative and recursive approaches |
| `Linked_list.py` | Singly linked list built from scratch: push, insert, delete, traverse |
| `maxfind.py` | Finding the maximum value in a list — manual and built-in approaches |
| `OOP.py` | Object-oriented programming basics — classes, `__init__`, methods, encapsulation |
| `binary_exponentiation.py` | Fast exponentiation (repeated squaring) — O(log n) vs O(n) |
| `recursion_basics.py` | Recursion fundamentals with classic examples |
| `Searching and sorting types.py` | Binary search + bubble, selection, and insertion sort implemented from scratch |
| `selection_sort.py` | Selection sort with step-by-step trace output |

---

## How to Run

**Requirements:** Python 3.x (no external libraries)

```bash
python fibonacci.py
python Linked_list.py
python "Searching and sorting types.py"
```

Most scripts print output directly. Some have examples commented out — uncomment lines to test different inputs.

---

## What I Learned

These scripts mark the early stages of my Python journey. Looking back at them, a few things stand out as turning points:

- **Loops and control flow** — understanding *when* to use `while` vs `for` rather than just knowing both exist
- **Recursion** — the moment it clicked that a function can call itself, and learning to trust the base case
- **Data structures from scratch** — building a linked list manually (with `Node` and `Linkedlist` classes) gave me a much deeper understanding of how Python's built-in lists actually work under the hood
- **Algorithm efficiency** — rewriting the same task (e.g. exponentiation, search) in O(n) and then O(log n) and *seeing* the difference in steps made Big-O feel real rather than abstract
- **OOP basics** — writing my first classes here is what set me up for the more complex inheritance work in the MIT course and the Fitness Tracker project

This repo is background material — the concepts here feed directly into the more applied work in the other repos.

---

## Related Repos

- [**fitness-tracker**](../fitness-tracker) — full OOP application built using these foundations
- [**mit-algorithms**](../mit-algorithms) — deeper algorithmic work building on these concepts

