class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __contains__(self, value):
        if self.head is None:
            return False
        last = self.head
        while last.next is not None:
            last = last.next
            if value == last.value:
                return True
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
            last.next = new_node
            self.size += 1

    #Inspect your mistake. Understand what happens when
    # you make the mistake of setting the last=last.next 
    # early instead of at the end of the loop.
    def delete(self, value):
        if value == self.head.value:
            self.head = self.head.next
        last = self.head
        while last.next is not None:
            if value == last.next.value:
                new_node = last.next.next
                last.next =new_node
            last = last.next

        
    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds!")
        if index == 0:
            return self.head.value
        last = self.head
        for i in range(index):
            last = last.next
        return last.value

    def insert(self, value, index):
        if index < 0 | index >= self.size:
            raise IndexError("Index out of bounds!")
        last = self.head
        if index == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        else:
            for i in range(index - 1):
                if last is None:
                    raise IndexError("Index is out of bounds!")
                last = last.next
            new_node = Node(value)
            if last.next is not None:
                new_node.next = last.next
            else:
                new_node.next = None
            last.next = new_node

    def pop(self, index):
        if index < 0 | index >= size | self.head is None:
            raise IndexError("Index out of bounds!")
        last = self.head
        for i in range(index - 1):
            last = last.next
        val = last.next.value
        new_node = last.next.next
        last.next = new_node
        return val

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
    
    def print(self):
        last = self.head
        ll = []
        while last.next is not None:
            ll.append(last.value)
            last = last.next
        ll.append(last.value)
        print(ll)

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.prepend(1)
    ll.prepend(0)
    ll.insert(6, 2)
    ll.delete(5)
    ll.print()

    get = ll.get(2)
    contains = ll.__contains__(4)
    info = ll.__repr__()
    val = ll.pop(2)
    size = ll.size
    print(get, size, contains, info, val)

# Footnotes:
# Take care to attempt to optimize this module as it is highly
# ineffient right now.😁😁😁Ganbatte!!, you're doing great!