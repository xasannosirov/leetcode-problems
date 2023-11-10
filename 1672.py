class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        res = -1
        for i in accounts:
            if res < sum(i):
                res = sum(i)
        return res
