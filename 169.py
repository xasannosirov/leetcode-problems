class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        res = 0
        count = 0
        check = set(nums)
        for i in check:
            if nums.count(i) > count:
                res = i
                count = nums.count(i)
        return res
