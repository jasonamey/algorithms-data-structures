class Solution:
    def rotate(self, arr: list[int], k: int) -> None:
      self.reverse_array(arr, 0, len(arr) - 1)
      self.reverse_array(arr, 0, k - 1)
      self.reverse_array(arr,k, len(arr) - 1)
    def reverse_array(self, arr: list[int], i: int, j: int):
      while (i < j):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1 
        j -= 1
        
s = Solution()

arr = [1,2,3,4,5,6,7]
s.rotate(arr, 3)
assert arr == [5,6,7,1,2,3,4]
        
arr = [-1,-100,3,99]
s.rotate(arr, 2)
assert arr == [3,99,-1,-100]

