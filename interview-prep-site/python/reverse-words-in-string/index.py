def getStringChunk(idx, str, isWhiteSpace):
    count = idx
    if (isWhiteSpace):
        while(count < len(str) and str[count] == " " ):
            count += 1
    else: 
        while(count < len(str) and str[count] != " "):
            count += 1

    return [count, str[idx:count]]
    
def reverseWordsInArray(arr):
    lastIdx = len(arr) - 1
    for i in range(0, int(lastIdx/2) + 1): 
        arr[i], arr[lastIdx - i] = arr[lastIdx - i], arr[i]
    return arr
    
def createFinalString(firstArray, secondArray):
    idx = 0 
    finalString = ""
    while idx < len(firstArray) and idx < len(secondArray):
        finalString += firstArray[idx] + secondArray[idx]
        idx += 1
    if idx < len(firstArray):
        finalString += firstArray[idx]
    if idx < len(secondArray):
        finalString += secondArray[idx]
    return finalString

def reverseWordsInString(string):
    if len(string) == 0: 
        return string
    whiteSpaces = []
    words = []
    isWhiteSpaceFirst = True if string[0] == " " else False
    idx = 0
    isWhiteSpace = isWhiteSpaceFirst
    
    while idx < len(string):
        if(isWhiteSpace): 
            charEnd, whiteSpace = getStringChunk(idx, string, True)
            whiteSpaces.append(whiteSpace)
            idx = charEnd
        else: 
            charEnd, word = getStringChunk(idx, string, False)
            words.append(word)
            idx = charEnd
        isWhiteSpace = not isWhiteSpace
        
    reversedWords = reverseWordsInArray(words)
    firstArray = whiteSpaces if isWhiteSpaceFirst else reversedWords
    secondArray = reversedWords if isWhiteSpaceFirst else whiteSpaces
    
    return createFinalString(firstArray, secondArray)
        
