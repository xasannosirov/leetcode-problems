class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        res = list()
        check = str()
        for i in range(len(s)):
            if s[i].isdigit():
                check += s[i]
            else:
                if len(check) > 0:
                    res.append(int(check))
                check = str()
        if len(check):
            res.append(int(check))
        if len(set(res)) != len(res):
            return False
        return res == sorted(res)
