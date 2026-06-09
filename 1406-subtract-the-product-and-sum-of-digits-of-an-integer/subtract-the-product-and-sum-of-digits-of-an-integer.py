class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0 
        prod = 1
        while n > 0:
            r = n % 10
            sum = sum + r
            prod = prod * r
            n = n // 10
        result = prod - sum
        return result
            
        