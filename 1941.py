class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        check = s.count(s[0])
        for i in s:
            if s.count(i) != check:
                return False
        return True
