def semordnilap(words):
    finalWords = []
    foundWords = set()
    for i in range(0, len(words)):
        if words[i] not in foundWords:
            reverse = reversedWord(words[i])
            for j in range(0, len(words)):
                if j == i:
                    continue
                if reverse == words[j]:
                    finalWords.append([words[i], reverse])
                    foundWords.add(words[j])
                    foundWords.add(reverse)
    return finalWords


def reversedWord(word):
    return "".join(list(reversed(word)))


a = ["dog", "aaa", "desserts", "god", "stressed"]
print(semordnilap(a))
