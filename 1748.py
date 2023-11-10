class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        res = list()
        for i in nums:
            if nums.count(i) == 1:
                res.append(i)
        return sum(res)
