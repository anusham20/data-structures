class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    Singly linked list implementation.
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        """Insert at head."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def search(self, value):
        """Return node if found, else None."""
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def delete(self, value):
        """Delete first occurrence of value."""
        current = self.head
        previous = None

        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def to_list(self):
        """Convert linked list to Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def __repr__(self):
        return f"LinkedList({self.to_list()})"