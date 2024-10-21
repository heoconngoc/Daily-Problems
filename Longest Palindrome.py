class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        count = 0
        for i in d:
            if d[i] % 2 == 0:
                count += d[i]
            else:
                count += d[i] - 1

        if count < len(s):
            count += 1
        return count 
