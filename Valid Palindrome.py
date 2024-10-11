class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leters = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s = s.lower()
        result = ''
        for char in s:
            if char in leters:
                result += char

        return result == result[::-1]
