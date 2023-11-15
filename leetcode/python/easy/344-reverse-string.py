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

def reverseString_recursive(s: list[str]) -> None:
  arr_len = len(s)
  if arr_len == 0 or arr_len == 1: 
    return 
  else: 
    s[0], s[arr_len - 1] = s[arr_len - 1], s[0]
    reverseString_recursive(s[1:arr_len-1])
  if arr_len == 3: 
    print(s)
    



