class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        one = list()
        two = list()
        for i in nums:
            if i % 2:
                two.append(i)
            else:
                one.append(i)
        one.sort()
        two.sort(reverse=True)
        return one + two
