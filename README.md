# 📚 Data Structures in Python

A clean, interview-ready implementation of fundamental data structures built from scratch.

This repository focuses on:
- Core data structure understanding
- Time complexity awareness
- Clean code design
- Edge case handling
- Simple test coverage

---

# 🧱 Implemented Data Structures

## 🥞 Stack (LIFO)
Last-In-First-Out structure.

Operations:
- `push()` → O(1)
- `pop()` → O(1)
- `peek()` → O(1)

Common Use Cases:
- Function call stack
- Undo/redo systems
- Expression parsing
- Backtracking algorithms

---

## 🚶 Queue (FIFO)
First-In-First-Out structure.

Operations:
- `enqueue()` → O(1)
- `dequeue()` → O(n) (list-based implementation)
- `front()` → O(1)

Common Use Cases:
- Scheduling
- Breadth-First Search (BFS)
- Task processing systems

---

## 🔗 Singly Linked List

A dynamic structure where nodes point to the next node.

Operations:
- Insert at head → O(1)
- Search → O(n)
- Delete → O(n)

Advantages:
- Dynamic size
- Efficient insertions
- No memory reallocation required

---

## 🌳 Binary Search Tree (BST)

An ordered binary tree where:

Left subtree < Node < Right subtree

Operations:
- Insert → O(log n) average
- Search → O(log n) average
- Inorder traversal → produces sorted output

Worst-case complexity (unbalanced tree):
- O(n)

---

# 📊 Time Complexity Summary

| Data Structure | Insert | Search | Delete |
|---------------|--------|--------|--------|
| Stack         | O(1)   | O(n)   | O(1)   |
| Queue         | O(1)   | O(n)   | O(n)   |
| Linked List   | O(1)*  | O(n)   | O(n)   |
| BST (average) | O(log n) | O(log n) | O(log n) |
| BST (worst)   | O(n)   | O(n)   | O(n)   |

\*Linked list insert shown is insert at head.

---

# 🧪 Running Tests

Navigate to the `src` directory:

cd src
python test_data_structures.py

If successful, you should see:

✓ Stack test passed  
✓ Queue test passed  
✓ Linked List test passed  
✓ BST test passed  

Edge cases are also tested (empty structures).

---

# 🎯 Demo

To see example usage:

cd src  
python demo.py  

---

# 🧠 Design Philosophy

This repository emphasizes:

- Clear implementation over shortcuts
- Explicit complexity awareness
- Readable, maintainable structure
- Interview-focused fundamentals

All data structures are implemented manually without external libraries.

---

# 🚀 Future Improvements

- Replace queue with `collections.deque` for O(1) dequeue
- Add AVL Tree
- Add Red-Black Tree
- Add Heap / Priority Queue
- Add Graph (BFS & DFS)
- Convert test suite to pytest
- Add benchmarking

---

# 👩‍💻 Author

Anusha Maheshwari  