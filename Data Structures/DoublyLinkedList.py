class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __contains__(self, value):
        last = self.head
        while last:
            if value == last.value:
                return True
            last = last.next
        return False

    def __repr__(self):
        if self.head is None:
            return "[]"
        last = self.head
        return_string = f"[{last.value}"
        while last.next is not None:
            last = last.next
            return_string += f", {last.value}"
        return_string += "]"
        return return_string

    def append(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.size += 1
        else:
            last = self.head
            while last.next is not None:
                last = last.next
            new_node = Node(value)
            new_node.previous = last
            last.next = new_node
            self.size += 1

    def delete(self, value):
        if self.head is None:
            return
        if value == self.head.value:
            self.head = self.head.next
            if self.head:
                self.head.previous = None
            self.size -= 1
            return

        last = self.head
        while last and last.next:
            if value == last.next.value:
                node_to_remove = last.next
                new_node = node_to_remove.next
                last.next = new_node
                if new_node:
                    new_node.previous = last
                self.size -= 1
                return
            last = last.next

    def get(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Index out of bounds!")
        if index == 0:
            return self.head.value
        last = self.head
        for i in range(index):
            last = last.next
        return last.value

    def insert(self, value, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds!")
        last = self.head
        if index == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            self.size += 1
        else:
            for i in range(index - 1):
                if last is None:
                    raise IndexError("Index is out of bounds!")
                last = last.next
            new_node = Node(value)
            if last.next is not None:
                new_node.next = last.next
                new_node.next.previous = new_node
            else:
                new_node.next = None
            new_node.previous = last
            last.next = new_node
            self.size += 1

    def pop(self, index):
        if index < 0 or index >= self.size or self.head is None:
            raise IndexError("Index out of bounds!")
        last = self.head
        if index == 0:
            if self.size > 1:
                val = self.head.value
                self.head = self.head.next
                self.head.previous = None
                self.size -= 1
                return val
            else:
                val = self.head.value
                self.head = None
                self.size -= 1
                return val
        for i in range(index - 1):
            last = last.next
        node_to_pop = last.next
        val = last.next.value
        new_node = node_to_pop.next
        last.next = new_node
        if new_node:
            new_node.previous = last
        self.size -= 1
        return val

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            self.size += 1
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            self.size += 1

if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.append(1)
    ll.print()
    x = ll.pop(0)
    print(ll.info())
    ll.append(2)
    ll.append(2)
    ll.print()
    print(ll.info())
