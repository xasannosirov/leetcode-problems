class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i
