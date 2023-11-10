class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        list1=list()
        if len(nums1)>len(nums2):
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    nums1.remove(nums2[i])
                    list1.append(nums2[i])
        else:
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    nums2.remove(nums1[i])
                    list1.append(nums1[i])
        return list1
