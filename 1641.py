import itertools

class Solution:
    def countVowelStrings(self, n: int) -> int:
        a=list("aeiou")
        r=list(itertools.combinations_with_replacement(a,n))
        return len(r)
