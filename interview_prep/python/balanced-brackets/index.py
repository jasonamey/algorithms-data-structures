def balancedBrackets(string):
    opened = "([{"
    closed = ")]}"
    stack = []
    for bracket in string:
        if bracket in opened:
            stack.append(bracket)
        elif bracket in closed:
            if len(stack) == 0:
                return False
            test = stack.pop()
            if opened.index(test) != closed.index(bracket):
                return False
    return len(stack) == 0
