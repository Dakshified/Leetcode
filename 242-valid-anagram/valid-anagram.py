class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        if len(s) != len(t):
            return False
        for ch in s :
            if ch not in dict1:
                dict1[ch] = 1
            else:
                dict1[ch] = dict1[ch] + 1
        for ch in t:
            if ch not in dict1:
                return False
            else:
                dict1[ch] = dict1[ch] - 1
        for i in dict1.values():
            if i != 0 :
                return False
        return True 