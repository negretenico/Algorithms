class Node:
    def __init__(self,left,right,value):
        self.value =value
        self.left =left
        self.right= right
class BST:
    def __init__(self):
        pass
    def inorder_walk(self,node:Node):
        # This will take theta(n) time
        if node is None:
            return
        self.inorder_walk(node.left)
        print(node.value)
        self.inorder_walk(node.right)
    def recursive_search(self,node:Node,value):
        if node is None or value == node.value:
            return node
        if value <node.value:
            return self.recursive_search(node.left, value)
        return self.recursive_search(node.right, value)
    def iterative_search(self,node:Node, value):
        while node is not None and value != node.value:
            if node.value < value:
                node = node.left
                continue
            node = node.right
        return node
    def tree_max(self,head):
        while head.right is not None:
            head = head.right
        return head.value
    def tree_min(self,head):
        while head.left is not None:
            head = head.left
        return head.value