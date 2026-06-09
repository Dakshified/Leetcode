class Solution:
    def countDigits(self, num: int) -> int:
        ans = []
        original = num
        while num > 0:
            r = num % 10
            ans.append(r)
            num = num//10
        count = 0
        for i in ans:
            if(original  % i == 0 ):
                count = count + 1
        return count 

        