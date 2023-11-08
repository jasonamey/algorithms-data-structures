# time O(n) space O(1)
def twoSum(numbers, target):
    i = 0 
    j = len(numbers) - 1
    sum = numbers[i] + numbers[j]
    while sum != target: 
        if sum > target: 
            j -= 1
        elif sum < target: 
            i += 1
        sum = numbers[i] + numbers[j]
    return [i+1, j+1]

assert twoSum([2,7,11,15], 9) == [1,2]
assert twoSum([2,3,4], 6) == [1,3]
assert twoSum([-1,0], -1) == [1,2]