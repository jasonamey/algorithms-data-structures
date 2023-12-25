def longestPalindromicSubstring(string):
    if len(string) == 1:
       return string
    if len(string) == 2 and string[0] == string[1]:
       return string
    max = 0
    maxStr = ""
    for i in range(1, len(string)):
        l = i - 1 
        r = i + 1 
        test = 1
        if test > max: 
           max = test
           maxStr = string[l:r]
        while (l > -1 and r < len(string) and string[l] == string[r]):
          
          test += 2
          if test > max: 
            max = test
            maxStr = string[l:r+1]
          l -= 1 
          r += 1 
        if i + 2 < len(string) and string[i] == string[i + 1]:
          l = i - 1
          r = i + 2 
          test = 2
          if test > max: 
             max = 2
             maxStr = string[i:i+2]
          while (l > -1 and r < len(string) and string[l] == string[r]):
            test += 2
            if test > max: 
              max = test
              maxStr = string[l:r+1]  
            l = i - 1
            r = i + 1

    return maxStr
          
print(longestPalindromicSubstring("aabccba"))