class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = 0
        origin= n
        while n>0:
            last_digit= n%10
            rev = (rev*10) + last_digit
            n = n//10
        return abs(origin - rev)
        