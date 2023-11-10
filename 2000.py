class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
            try:
                i = word.index(ch)
                word = word[:i+1][::-1] +word[i+1:]
            except:
                return word
            else:
                return word
