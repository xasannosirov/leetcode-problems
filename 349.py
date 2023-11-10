class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = list()
        for i in nums1:
            if i in nums2:
                res.append(i)
        
        res = set(res)
        return res
