def getNthFib_ONE(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return getNthFib(n-1) + getNthFib(n-2)

def getNthFib(n):
    c = { 1: 0, 2: 1, 3: 1}
    return helper(n, c)


def helper(n, cache): 
    if n in cache: 
        return cache[n]
    else: 
        cache[n] = helper(n - 1, cache) + helper(n - 2, cache)
        return cache[n]

