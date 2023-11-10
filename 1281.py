class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sub = 1
        add = 0
        for i in str(n):
            sub *= int(i)
            add += int(i)
        return sub-add
