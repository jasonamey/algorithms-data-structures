# O(n) time and O(n) space
def bestDigits(number, numDigits):
    stack = []
    count = numDigits
    for digit in number:
        while count > 0 and len(stack) > 0 and int(stack[-1]) < int(digit):
            stack.pop()
            count -= 1
        stack.append(digit)
    while count > 0:
        stack.pop()
        count -= 1
    return "".join(stack)