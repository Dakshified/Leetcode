class Solution:
    def fib(self, n: int) -> int:
        if (n==0  or n==1): #base case
            return n
        return self.fib(n-1) + self.fib(n-2) #recursive case
        