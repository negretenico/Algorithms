class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
    def search(self,k):
        head = self.head
        while head != None and head.value !=k:
            head = head.next 
        return head
    def prepend(self, new_node:Node)->None:
        new_node.next = self.head
        new_node.prev = None
        if self.head != None:
            self.head.prev = new_node
        self.head = new_node
    def delete(self,new_node)-> None:
        if new_node.prev != None:
            new_node.prev.next = new_node.next
        else: 
            self.head = new_node.next
        if new_node.next !=  None:
            new_node.next.prev = new_node.prev
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return " -> ".join(map(str, values))