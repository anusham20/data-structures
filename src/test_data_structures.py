from stack import Stack
from queue import Queue
from linked_list import LinkedList
from bst import BST


def test_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.peek() == 1
    print("✓ Stack test passed")


def test_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.front() == 2
    print("✓ Queue test passed")


def test_linked_list():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    assert ll.search(10) is not None
    assert ll.delete(10)
    assert ll.to_list() == [20]
    print("✓ Linked List test passed")


def test_bst():
    tree = BST()
    tree.insert(10)
    tree.insert(5)
    tree.insert(20)
    assert tree.search(5) is not None
    assert tree.search(100) is None
    assert tree.inorder() == [5, 10, 20]
    print("✓ BST test passed")


if __name__ == "__main__":
    test_stack()
    test_queue()
    test_linked_list()
    test_bst()