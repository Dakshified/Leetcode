class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l=0
        r= int(sqrt(c))
        while l<= r:
            if l *l + r*r == c:
                return True
            if l*l + r*r < c :
                l = l+1
            if l*l +r*r > c:
                r = r-1
        return False
        