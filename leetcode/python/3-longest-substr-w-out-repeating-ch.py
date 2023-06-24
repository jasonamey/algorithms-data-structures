####INCORRECT SO FAR###########

# def lengthOfLongestSubstring(s):
#     characters = set()
#     i = 0
#     j = 0
#     max = 1 if len(s) > 0 else 0
#     while j < len(s) and i < len(s):
#         char = s[j]
#         if char not in characters:
#             characters.add(char)
#             tempMax = j - i + 1
#             max = tempMax if tempMax > max else max
#             j += 1
#         else:
#             if s[i] == char:
#                 i += 1
#             else :
#                 if i < j:
#                     while char != s[i]:
#                         characters.remove(s[i])
#                         i += 1
#                 i += 1
#                 else:
#                     j += 1
#     return max


print(lengthOfLongestSubstring("dvdf"))
