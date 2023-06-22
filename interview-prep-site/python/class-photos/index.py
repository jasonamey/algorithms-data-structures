r = [3, 8, 1, 3, 4]
b = [6, 9, 2, 4, 5]

b = [5, 8, 1, 3, 4, 9]
r = [6, 9, 2, 4, 5, 1]

b = [1, 3, 4, 5, 8, 9]
r = [1, 2, 4, 5, 6, 9]

def classPhotos(redShirtHeights, blueShirtHeights):
    r = redShirtHeights
    b = blueShirtHeights
    r.sort()
    b.sort()
    allTall = True
    allShort = True 
    for i in range(0, len(r)): 
        if(r[i] >= b[i]):
            allShort = False
        if(r[i] <= b[i]):
            allTall = False
    return allTall or allShort

print(classPhotos(r, b))