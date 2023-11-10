class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        res = list()
        for i in range(len(nums)):
            res.append(abs(sum(nums[:i]) - sum(nums[i+1:])))
        return res
