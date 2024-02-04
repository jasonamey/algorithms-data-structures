def minRewards(scores):
    if len(scores) == 0: 
        return 0
    if len(scores) == 1: 
        return 1
    points = ["" for _ in range(len(scores))]
    treats = [0 for _ in range(len(scores))]
    points[0] = "P" if scores[1] < scores[0] else "V"
    points[-1] = "P" if scores[-2] < scores[-1] else "V"
    idxV = []
    idxP = []
    for i in range(1, len(scores) -1):
        if scores[i] < scores[ i - 1] and scores[i] < scores[i + 1]:
            points[i] = "V"
        if scores[i] > scores[ i - 1] and scores[i] > scores[i + 1]:
            points[i] = "P"
    for i in range(0, len(points)):
        if points[i] == "V": 
            idxV.append(i)
        if points[i] == "P":
            idxP.append(i)
    for i in idxV: 
        treats[i] = 1
        left = i - 1 
        leftCount = 2
        right = i + 1 
        rightCount = 2
        while left > 0 and points[left] != "P":
            treats[left] = leftCount 
            leftCount += 1 
            left -= 1
        while right < len(scores) - 1 and points[right] != "P": 
            treats[right] = rightCount
            rightCount += 1 
            right += 1
    for i in idxP:
        if i == 0: 
            treats[i] = treats[i + 1] + 1
        elif i == len(scores) - 1: 
            treats[i] = treats[i - 1] + 1
        else:
            val = max(treats[i-1], treats[i+1])
            treats[i] = val + 1
    return sum(treats)
           
      