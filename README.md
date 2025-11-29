# ALGORITHM DESIGN & IMPLEMENTATION

This repository is a curated collection of fundamental **Data Structures** and **Algorithm Implementations**, focusing on efficient solutions for common algorithmic design problems. All implementations are written in Python and rigorously tested.

## Repository Contents

The algorithms and data structures are organized by topic for easy navigation.

---

### Data Structures (`data_structures/`)

This directory is divided into **Core**, **Graphs**, **Specialized**, and **Trees**.

#### **Core Implementations (`data_structures/core`)**

This folder contains the foundational, universal structures.

| File | Implements | Key Features |
| :--- | :--- | :--- |
| `array.py` | **StaticArray**, **DynamicArray** | Fixed-capacity array and a resizing array (Python `list` simulation). |
| `linked_list.py`| **Singly**, **Doubly**, **Circular** Linked Lists | Complete $O(1)$ operations at head/tail. |
| `stack.py` | **Stack (LIFO)** | Array-based implementation for $O(1)$ amortized performance. |
| `queue.py` | **Queue (FIFO)** | Doubly Linked List-based implementation for $O(1)$ performance. |
| `hash_table.py` | **HashTable**, **HashTableProbing**| Two implementations: Separate Chaining (SLL buckets) and Open Addressing (Linear Probing). |
| `heap.py` | **MaxHeap**, **MinHeap** | Array-based implementation for $O(\log N)$ priority queue operations. |

#### **Hierarchical Structures (`data_structures/trees`)**

| File | Implements | Status |
| :--- | :--- | :--- |
| `binary_search_tree.py`| Binary Search Tree (BST) | *To be implemented.* |
| `avl_tree.py` | AVL Tree | *To be implemented.* |
| `red_black_tree.py`| Red-Black Tree | *To be implemented.* |
| `b_tree.py` | B-Tree | *To be implemented.* |

#### **Graph Structures (`data_structures/graphs`)**

| File | Implements | Status |
| :--- | :--- | :--- |
| `adjacency_list.py` | Graph | *To be implemented.* |
| `adjacency_matrix.py`| Graph | *To be implemented.* |
| `disjoint_set_union.py`| DSU / Union-Find | *To be implemented.* |

---

### Algorithms (`algorithms/`)

| Directory | Focus | Status |
| :--- | :--- | :--- |
| `searching/` | Binary Search, Linear Search, Graph Traversal (BFS/DFS). | *To be implemented.* |
| `sorting/` | Merge Sort, Quick Sort, Heap Sort, etc. | *To be implemented.* |
| `greedy/` | Algorithms utilizing the Greedy approach. | *To be implemented.* |
| `miscellaneous/` | Other important algorithms (e.g., String Matching, Geometry). | *To be implemented.* |

---

### Testing (`tests/`)

| File | Validates | Status |
| :--- | :--- | :--- |
| `test_array.py` | StaticArray, DynamicArray | **Complete** |
| `test_linked_list.py` | SLL, DLL, CLL | **Complete** |
| `test_stack.py` | Stack (LIFO) | **Complete** |
| `test_queue.py` | Queue (FIFO) | **Complete** |
| `test_hashtable.py` | HashTable (Chaining), HashTableProbing (Linear Probing) | **Complete** |
| `test_heap.py` | MaxHeap, MinHeap | **Complete** |

---

## Getting Started

To explore and run the algorithms, follow these simple setup steps.

### Prerequisites

You will need **Python 3.x** installed on your system.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/CasuallyDreamin/algorithm_design.git
    cd algorithm-design
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies** (Ensure `requirements.txt` includes `pytest`):
    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

You can verify the correctness of any implemented data structure using the unit tests located in the `tests/` directory. We use `pytest` for testing.

```bash
# Ensure you have pytest installed
pip install pytest

# Run all tests
pytest