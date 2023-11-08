# time O(n) space O(1)
def reverseString(s: list[str]) -> None:
  last_idx = len(s) - 1
  for i in range(int(len(s)/2)): 
    s[i], s[last_idx - i] = s[last_idx - i], s[i]

str = ["h","e","l","l","o"]
reverseString(str) 
assert str == ["o","l","l","e","h"]

str = ["H","a","n","n","a","h"]
reverseString(str)
assert str == ["h","a","n","n","a","H"]
