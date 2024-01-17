def oneEdit(stringOne, stringTwo):
    a = [[0 for _ in range(len(stringOne) + 1) ] for _ in range(len(stringTwo) + 1)]
    stringOne = " " + stringOne
    stringTwo = " " + stringTwo 
    for i in range(0, len(stringOne)):
        a[0][i] = i
    for i in range(0, len(stringTwo)):
        a[i][0] = i  
    for j in range(1, len(stringTwo)):
        for i in range(1, len(stringOne)):
            candidate = min(a[j][i-1], a[j-1][i-1], a[j-1][i])
            if stringTwo[j] == stringOne[i]:
                a[j][i] = a[j-1][i-1]
            else: 
                a[j][i] = candidate + 1 
    for i in a:
        print(i)
    return a[len(a) - 1][len(a[0]) - 1] <= 1

assert oneEdit("a", "a") == True 
assert oneEdit("aaa", "aaa") == True
assert oneEdit("a", "b") == True
assert oneEdit("a", "ab") == True
assert oneEdit("abc", "b") == False
assert oneEdit("helo", "helle") == False