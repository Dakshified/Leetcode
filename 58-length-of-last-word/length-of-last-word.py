class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        n = len(s)
        i = -1
        s = s.strip()
        while (i >= (-1)*n and s[i] != " "):
            i = i - 1
        i = i + 1

        return i*(-1) 
        