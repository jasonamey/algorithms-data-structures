from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int):
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.popleft()) 

    def pop(self) -> int:
        if self.q1:
          return self.q1.popleft()

    def top(self) -> int:
        top = None
        if self.q1:
          top = self.q1.popleft()
          self.push(top)
        return top
            
    def empty(self) -> bool:
        return len(self.q1) == 0
        
stack = MyStack()

stack.push(1)
assert stack.top() == 1
stack.push(2)
assert stack.top() == 2
stack.push(3)
assert stack.pop() == 3
assert stack.empty() == False
assert stack.pop() == 2
assert stack.empty() == False
assert stack.pop() == 1
assert stack.empty() == True
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()