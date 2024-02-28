class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None for _ in range(k)]
        self.front = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else: 
            self.q[self.getBack()] = value
            self.size += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else: 
            self.q[self.front] = None
            self.front = (self.front + 1) % len(self.q)
            self.size -= 1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else: 
            return self.q[self.front]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else: 
            return self.q[(self.front + self.size - 1) % len(self.q)]
        
    def isEmpty(self) -> bool:
        return self.size == 0
        
    def isFull(self) -> bool:
        return self.size == len(self.q)
        
    def getBack(self): 
        return (self.front + self.size) % len(self.q)
    
    def __str__(self):
        return f"{self.q}"
    
    def __lt__(self, other):
        if len(self.q) < len(other.q):
            return True 
        else: 
            return False 
        