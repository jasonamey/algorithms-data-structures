def isValidSubsequence(array, sequence):
    i = 0
    j = 0 
    while i < len(array) and j < len(sequence):
        print(i, j)
        if array[i] == sequence[j]:
            i += 1
            j += 1
        else: 
            i += 1 
    return j == len(sequence)
