class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = float('inf')
        res = 0
        for i in range(n-2):
            left = i+1
            right = n-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(target-s) < diff:
                    diff = abs(target - s)
                    res = s
                if s < target:
                    left+=1
                else:
                    right-=1
        return res
