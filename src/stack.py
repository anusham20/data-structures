class Stack:
    """
    Stack implementation using Python list.
    LIFO (Last In First Out).
    """

    def __init__(self):
        self._items = []

    def push(self, value):
        """Push value onto stack."""
        self._items.append(value)

    def pop(self):
        """Remove and return top element."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return top element without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __repr__(self):
        return f"Stack({self._items})"