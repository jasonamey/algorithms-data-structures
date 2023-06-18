def findClosestValueInBst(tree, target):
    value = tree.value
    dif =  2 ** 63 - 1
    while (tree is not None):
        if tree.value == target: return target
        else :
            testDif = abs(tree.value - target)
            if (testDif < dif):
                dif = testDif
                value = tree.value
            if (target < tree.value):
                tree = tree.left
            else:
                tree = tree.right
    return value