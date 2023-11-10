class Solution:
    def sortSentence(self, s: str) -> str:
        a = s[::-1].split() 
        a.sort()
        r = list()
        for i in a:
            r.append(i[1:][::-1])
            
        return " ".join(r)
