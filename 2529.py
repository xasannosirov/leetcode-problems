class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        positive = 0
        negative = 0
        for i in nums:
            if i > 0:
                positive += 1
            elif i < 0:
                negative += 1
        
        if (positive) > (negative):
            return (positive)
        else:
            return (negative)
