class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res = list()
        for i in range(len(nums)):
            summa = 0
            for j in nums[:i+1]:
                summa += j
            res.append(summa)
        return res
