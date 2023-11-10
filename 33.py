class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
        return -1
