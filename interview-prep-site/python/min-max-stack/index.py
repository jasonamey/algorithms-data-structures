class MinMaxStack:
    def __init__(self):
        self.stack = []

    def peek(self):
        return self.stack[-1][0]

    def pop(self):
        if self.stack:
            item = self.stack.pop()
            return item[0]
        else:
            print("stack is empty")

    def push(self, number):
        if len(self.stack) == 0:
            self.stack.append([number, [number, number]])
        else:
            min = self.getMin()
            max = self.getMax()
            if number < min:
                min = number
            if number > max:
                max = number
            self.stack.append([number, [min, max]])

    def getMin(self):
        if self.stack:
            return self.stack[-1][1][0]
        else:
            print("stack is empty")

    def getMax(self):
        if self.stack:
            return self.stack[-1][1][1]
        else:
            print("stack is empty")


s = MinMaxStack()
s.push(1)
s.push(3)
s.push(-2)
s.push(10)
print(s.getMin())
print(s.getMax())
print(s.peek())
print(s.stack)
