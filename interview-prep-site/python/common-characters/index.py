def commonCharacters(strings):
    minIdx = 0
    minNum = len(strings[0])
    for i in range(1, len(strings)):
        if len(strings[i]) < minNum:
            minIdx = i
            minNum = len(strings[i])
    smallCharSet = set(strings[minIdx])
    for i in range(1, len(strings)):
        if i == minIdx:
            continue
        compareSet = set(strings[i])
        charactersToRemove = []
        for char in smallCharSet:
            if char not in compareSet:
                charactersToRemove.append(char)
        for char in charactersToRemove:
            smallCharSet.remove(char)
    return list(smallCharSet)


# s = ["abc", "bcd", "cbad"]
# print(commonCharacters(s))
