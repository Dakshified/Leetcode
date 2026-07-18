class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        rev = nums[ : ]
        n = len(nums)
        i = 0
        j = n-1
        while i< j:
            rev[i],rev[j] = rev[j],rev[i]
            i = i+1
            j = j-1
        return nums+ rev


        
        