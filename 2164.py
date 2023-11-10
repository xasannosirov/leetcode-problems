class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        odd = list()
        even = list()
        res = list()
        for i in range(len(nums)):
            if i % 2:
                odd.append(nums[i])
            else:
                even.append(nums[i])
        odd = sorted(odd, reverse=True)
        even = sorted(even)
        for j in range(len(odd)):
            res.append(even[j])
            res.append(odd[j])
        for i in nums:
            if nums.count(i) != res.count(i):
                res.append(i)
        return res
