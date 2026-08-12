class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        w = (word[::-1] for word in a)

        return " ".join(w)
        