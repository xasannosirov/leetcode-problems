class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        res = list()
        for i in mat:
            for j in i:
                res.append(j)
        if len(res) != r*c:
            return mat
        else:
            result = list()
            l = 0
            for i in range(r):
                row = list()
                for j in range(c):
                    row.append(res[l])
                    l+=1
                result.append(row)
        return result
