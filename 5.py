class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = str()
        if s == s[::-1]:
            return s
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i:j+1] == s[i:j+1][::-1] and len(s[i:j+1]) > len(res):
                    res = s[i:j+1]
        return res 
