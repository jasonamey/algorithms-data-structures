def minimumWaitingTime(queries):
    queries.sort()
    print(queries)
    total = 0
    for i in range(0, len(queries) - 1): 
        print(i, " ", len(queries) - 1 - i, " ", queries[i] * len(queries) - 1 - i) 
        total += queries[i] * (len(queries) - 1 - i )
    return total


# a = [3, 2, 1, 2, 6]
# print(minimumWaitingTime(a))
    
