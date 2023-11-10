class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = str()
        for i in address:
            if i == ".":
                res += "["
                res += '.'
                res += ']'
            else:
                res += i
        return res
