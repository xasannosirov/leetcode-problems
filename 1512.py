class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        res = dict()
        for i in nums:
            if nums.count(i) > 1:
                res[i] = nums.count(i)
        res = res.values()
        summa = 0
        for k in res:
            if k == 2:
                summa += 1
            elif k == 3:
                summa += 3
            else:
                k -=1
                while k > 0:
                    summa += k
                    k-=1
        return summa
