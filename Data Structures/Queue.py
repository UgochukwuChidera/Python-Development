class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def __repr__(self):
        items = []
        current = self.front
        while current is not None:
            items.append(str(current.value))
            current = current.next
        return " -> ".join(items)
    
    def enqueue(self, value):
        if self.front is None:
            self.front = self.rear = Node(value)
        else:
            new_node = Node(value)
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    
    def dequeue(self):
        if self.front is None:
            raise ValueError("No items in the queue to pop!")
        
        node_to_remove = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None

        self.size -= 1
        return node_to_remove.value

    def peek(self):
        if self.front is None:
            raise ValueError("No items in the queue to pop!")
        
        return self.front.value

    def is_empty(self):
        return self.front is None

que = Queue()
print(que.is_empty())
que.enqueue(3)
print(que.is_empty())
que.enqueue(6)
que.enqueue(9)
que.enqueue(12)
que.enqueue(15)
que.enqueue(16)
print(que.__repr__())
print(que.__len__())
print(que.dequeue())
print(que.dequeue())
print(que.__len__())
print(que.peek())
print(que.__repr__())
