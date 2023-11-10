class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {' ' : ' '}
        key = key.replace(' ', '')
        l = 97
        for i in key:
            if i not in d:
                d[i] = chr(l)
                l+=1
        s = str()
        for i in message:
            s += d[i]
        return s
