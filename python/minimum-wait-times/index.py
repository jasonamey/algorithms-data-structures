def minimumWaitingTime(queries):
    queries.sort()
    total = 0
    for i in range(0, len(queries) - 1): 
        total += queries[i] * (len(queries) - 1 - i )
    return total


# a = [3, 2, 1, 2, 6]
# print(minimumWaitingTime(a))
    
