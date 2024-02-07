class Solution:
    def evalRPN(self, tokens) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        temp = []
        for ch in tokens:
            if ch not in "*-/+":
                temp.append(ch)
            else: 
              if len(temp) >= 2:
                  item1 = int(temp.pop())
                  item2 = int(temp.pop())
                  if ch == "+":
                      temp.append(item1 + item2)
                  if ch == "/":
                      temp.append(item2 / item1)
                  if ch == "*":
                      temp.append(item1 * item2)          
                  if ch == "-":
                      temp.append(item2 - item1)
        return int(temp[0])

s = Solution()

assert s.evalRPN(["2","1","+","3","*"]) == 9
assert s.evalRPN(["4","13","5","/","+"]) == 6
assert s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22