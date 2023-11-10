class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        res = list()
        for i in arr2:
            new = list()
            for j in arr1:
                if i == j:
                    res.append(j)
                else:
                    new.append(j)
            arr1 = new
        return res + sorted(arr1)
