class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd =0
        sum_even= 0
        odd =1
        even= 2
        for i in range(n):
            sum_odd =sum_odd +odd
            odd = odd + 2
        for i in range(n):
            sum_even = sum_even + even
            even = even + 2
        while sum_even != 0:
            temp = sum_even
            sum_even = sum_odd % sum_even
            sum_odd = temp
        return sum_odd