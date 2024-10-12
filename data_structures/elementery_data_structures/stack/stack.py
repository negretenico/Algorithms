class Stack:
    def __init__(self,n:int):
        self.size = n
        self.top = -1
        self.stackk = []
    def is_empty(self) -> bool:
        return self.top == -1
    def push(self,item):
        if self.top == self.size-1:
            raise Exception("OVERFLOW")
        self.top = self.top+1
        self.stackk.append(item)
    def pop(self):
        if self.is_empty():
            raise Exception("UNDERFLOW")
        self.top = self.top -1
        item = self.stackk.pop()
        return item