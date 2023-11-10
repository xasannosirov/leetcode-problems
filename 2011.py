class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        res = 0
        for i in operations:
            if i[0] == i[1] and i[0] == "-":
                res -= 1
            elif i[0] == i[1] and i[0] == '+':
                res += 1
            elif i[1] == i[2] and i[1] == "+":
                res += 1
            elif i[1] == i[2] and i[1] == '-':
                res -= 1
                
        return res
