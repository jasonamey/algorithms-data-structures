class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []  

    def push(self, x: int):
        while self.s1: 
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
      
    def pop(self) -> int:
        if self.s1:
            return self.s1.pop()
        else:
            return None
  
    def peek(self) -> int:
        return self.s1[-1]
            
    def empty(self) -> bool:
        return len(self.s1) == 0
  
    def __str__(self):
        return f"{self.s1}"
    
queue = MyQueue()
queue.push(1)
assert queue.peek() == 1
queue.push(2)
queue.push(3)
queue.push(4)
assert queue.empty() == False
assert queue.pop() == 1
assert queue.empty() == False
assert queue.pop() == 2
assert queue.pop() == 3
assert queue.pop() == 4
assert queue.empty() == True

        
