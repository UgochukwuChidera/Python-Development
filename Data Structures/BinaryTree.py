class Node:
    def __init__(self, key):
        self.key = key
        self.value = None
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.key} --> {self.value}"
    
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
        # self.height = 0

    def __contains__(self, key):
        current_node = self.root

        while True:
            if key < current_node:
                current_node = current_node.left
            elif key > current_node:
                current_node = current_node.right
            else:
                return True
            
        return False


    def __iter__(self):
        pass

    def __repr__(self):
        pass

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key)
            self.root.value = value
        else:
            current_node = self.root
            while True:
                if key < current_node.key:
                    if current_node.left is None:
                        current_node.left = Node(key)
                        current_node.left.value = value
                        current_node.left.parent = current_node
                        self.size += 1
                        break
                    else:
                        current_node = current_node.left
                elif key > current_node.key:
                    if current_node.right is None:
                        current_node.right = Node(key)
                        current_node.right.value = value
                        current_node.right.parent = current_node
                        self.size +=1 
                        break
                    else:
                        current_node = current_node.right
                else:
                    current_node.value = value

    def search(self, key):
        current_node = self.root
        while True:
            if current_node is None or current_node.key == key:
                return current_node
            elif key < current_node:
                if current_node.left is None:
                    return None
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    return None
                else:
                    current_node = current_node.right
    def delete(self, key):
        pass

    def traverse(self, order):
        pass

    def _delete(self, key):
        pass

    def _successor(self, node):
        pass

    def _predecessor(self, node):
        pass

    def _in_order_traversal(self):
        pass
    def _pre_order_traversal(self):
        pass
    def _post_order_traversal(self):
        pass
