def threeNumberSort(array, order):
    first = order[0]
    middle = order[1]
    f = 0
    m = 0
    l = len(array) - 1
    while m <= l:
        if array[m] == first:
            swap(f, m, array)
            m += 1
            f += 1
        elif array[m] == middle:
            m += 1
        else:
            swap(l, m, array)
            l -= 1
    return array


def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# print(threeNumberSort([1, 0, -1, 1, 1, 0, 0, 0, -1], [1, 0, -1]))
