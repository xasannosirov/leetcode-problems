class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ans = list()
        for i in s:
            if i in ans:
                return i
            else:
                ans.append(i)
