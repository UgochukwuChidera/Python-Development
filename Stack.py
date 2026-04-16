class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def __repr__(self):
        last = self.top
        if last is None:
            return "No elements in the stack!"
        elems = []
        while last is not None:
            value = last.value
            elems.append(str(value))
            last = last.next
        return ", ".join(elems)

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
            self.size += 1
            return
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        if self.size <= 0:
            raise ValueError("No items in the stack to pop!")
        val = self.top.value
        self.top = self.top.next
        self.size -= 1
        return val

    def peek(self):
        if self.size <= 0:
            raise ValueError("No items in the stack to peek!")
        val = self.top.value
        return val

stack = Stack()
print(stack.is_empty())
stack.push(5)
print(stack.is_empty())
stack.push(25)
stack.push(15)
print(stack.__len__())
print(stack.__repr__())
print(stack.peek())
print(stack.pop())
print(stack.__repr__())