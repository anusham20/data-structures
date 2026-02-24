# Data Structures in Python

This repository contains clean, interview-ready implementations of fundamental data structures.

---

# Implemented Structures

- Stack (LIFO)
- Queue (FIFO)
- Singly Linked List
- Binary Search Tree (BST)

---

# Concepts Explained

## Stack
Last-In-First-Out structure.
Operations:
- push → O(1)
- pop → O(1)
- peek → O(1)

Used in:
- Function calls
- Expression evaluation
- Backtracking

---

## Queue
First-In-First-Out structure.
Operations:
- enqueue → O(1)
- dequeue → O(n) (list-based implementation)

Used in:
- Scheduling
- Breadth-first search

---

## Linked List
Nodes connected via pointers.
Operations:
- insert at head → O(1)
- search → O(n)
- delete → O(n)

Advantages:
- Dynamic size
- Efficient insertions

---

## Binary Search Tree
Ordered tree structure.
Left subtree < node < right subtree.

Operations:
- insert → O(log n) average
- search → O(log n) average
- inorder traversal → produces sorted list

Worst case (unbalanced) → O(n)

---

# Running Tests

cd src  
python test_data_structures.py

If all tests pass, you will see:

✓ Stack test passed  
✓ Queue test passed  
✓ Linked List test passed  
✓ BST test passed  

---

# Future Improvements

- Use collections.deque for O(1) queue dequeue
- Add balanced BST (AVL or Red-Black)
- Add Heap
- Add Graph
- Convert to pytest
- Add performance benchmarking

---

Author: Anusha Maheshwari