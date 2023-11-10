class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        thisStr = str()
        while len(s):
            if len(s) >= 2*k:
                thisStr += s[:k][::-1] + s[k:2*k]
                s = s[2*k:]
            elif len(s) < 2*k and len(s) >= k:
                thisStr += s[:k][::-1] + s[k:]
                break
            elif len(s) < k:
                thisStr += s[::-1]
                break

        return thisStr
