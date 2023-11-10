class Solution:
    def hcfnaive(self, a, b):
        if(b == 0):
            return abs(a)
        else:
            return self.hcfnaive(b, a % b)

    def findGCD(self, nums: list[int]) -> int:
        return self.hcfnaive(max(nums), min(nums))
