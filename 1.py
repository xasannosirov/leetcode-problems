class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 2 and sum(nums) == target:
            return [0,1]
        res = list()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    res = [i,j]
        return res
