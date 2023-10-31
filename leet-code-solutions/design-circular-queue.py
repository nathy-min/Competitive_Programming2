class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False 
        if len(self.queue) < self.k:
            self.queue.append(value)
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if len(self.queue) > 0:
            self.queue.pop(0)
            return True

    def Front(self) -> int:
        if len(self.queue) > 0:
            return self.queue[0]
        return -1

    def Rear(self) -> int:
        if len(self.queue) > 0:
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True

    def isFull(self) -> bool:
        if len(self.queue) == self.k:
            return True

