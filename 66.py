class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        res = str()
        for i in digits:
            res += str(i)
        res = str(int(res)+1)
        lst = list()
        for i in res:
            lst.append(int(i))
        return lst
