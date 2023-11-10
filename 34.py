class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        num1 = -1
        num2 = -1
        for i in range(len(nums)):
            if nums[i] == target and num1 == -1:
                num1 = i
            elif nums[i] == target and num1 != -1:
                num2 = i
        if num1 != -1 and num2 == -1:
            return [num1, num1]
        elif num1 == -1 and num2 != -1:
            return [num2, num2]
        return [num1, num2] 
