def sortedSquares(self, nums: list[int]) -> list[int]:
    l = 0
    r = len(nums) - 1
    answer = []
    while l <= r: 
        square_left = nums[l] * nums[l]
        square_right = nums[r] * nums[r]
        if square_left > square_right: 
            answer.append(square_left)
            l += 1
        else: 
            answer.append(square_right)
            r -= 1
    return answer[::-1]

def sortedSquares_logan(self, nums: list[int]) -> list[int]:
  left = 0
  right = len(nums) - 1
  result = [0] * len(nums)
  index = len(nums) - 1

  while left <= right:
    left_square = nums[left] * nums[left]
    right_square = nums[right] * nums[right]
    if left_square > right_square:
      result[index] = left_square
      left += 1
    else:
      result[index] = right_square
      right -= 1
    index -= 1

  return result

assert sortedSquares([-4,-1,0,3,10]) == [0, 1, 9, 16, 100]
assert sortedSquares([-7,-3,2,3,11]) == [4, 9, 9, 49, 121]

assert sortedSquares_logan([-4,-1,0,3,10]) == [0, 1, 9, 16, 100]
assert sortedSquares_logan([-7,-3,2,3,11]) == [4, 9, 9, 49, 121]