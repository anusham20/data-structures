class Queue:
    """
    Queue implementation using Python list.
    FIFO (First In First Out).
    """

    def __init__(self):
        self._items = []

    def enqueue(self, value):
        """Add element to back of queue."""
        self._items.append(value)

    def dequeue(self):
        """Remove and return front element."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._items.pop(0)

    def front(self):
        """Return front element without removing."""
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __repr__(self):
        return f"Queue({self._items})"