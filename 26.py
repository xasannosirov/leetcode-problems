class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
            temp = set(nums)
            nums.clear()
            for i in temp:
                nums.append(i)
            nums.sort()
            return len(nums)
