from itertools import permutations

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = list()
        res2 = list()
        for i in permutations(nums):
            res.append(list(i))
        for i in res:
            if i not in res2:
                res2.append(i)
        return res2
