class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

or

class Solution(object):
    def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        result = ''
        if (len(t) != len(s)):
          return False
        for char in s:
          if char in t:
            t = t.replace(char, '',1)
            s = s.replace(char,'',1)
            result = True
          else:
            return False
        return result
    
