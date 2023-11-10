class Solution:
    def calPoints(self, operations: list[str]) -> int:
        res = list()
        for i in operations:
            if i == "+":
                res.append(res[-1]+res[-2])
            elif i == "C":
                res.pop()
            elif i == "D":
                res.append(res[-1]*2)
            elif len(i) == 1 and 0 <= int(i) <= 9:
                res.append(int(i))
            elif len(i) > 1 and i[0] == "-":
                x = int(i[1:])*-1
                res.append(x)
            elif len(i) > 1 and i[0] != "-":
                res.append(int(i))
        return sum(res)
