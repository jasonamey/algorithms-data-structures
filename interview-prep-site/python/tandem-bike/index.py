r = [5, 5, 3, 9, 2] 
b = [3, 6, 7, 2, 1]

# r = [2, 3, 5, 5, 9]
# b = [7, 6, 3, 2, 1]

r = [5, 5, 3, 9, 2]
b = [3, 6, 7, 2, 1]


#largest number always wins, is the "fastest"... for "slowest", try to knock out complimentary "higher" numbers

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    r = redShirtSpeeds
    b = blueShirtSpeeds
    r.sort()
    b.sort(reverse=(fastest))
    total = 0
    for i in range(0, len(r)):
          total += max(r[i], b[i])
    return total

# print(tandemBicycle(r, b, True))
