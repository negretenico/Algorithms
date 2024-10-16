class Queue:
    def __init__(self):
        self.head = 0 
        self.tail = 0 
        self.__queue = []
    def enqueue(self,x):
        self.__queue.append(x)
        self.tail = (self.tail +1) % len(self.__queue)
    def dequeue(self):
        if not self.__queue:
            raise IndexError("Queue is empty")
        x = self.__queue[self.head]
        self.head = (self.head+1) % len(self.__queue)
        return x
    def get_queue(self):
        return self.__queue