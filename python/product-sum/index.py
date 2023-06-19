def productSum(array):
    return helper(1, array)

def helper(size, array):
    total = 0
    for i in array:
        if isinstance(i, int): 
            total += i
        else:
            total += helper(size + 1, i)
    return total * size