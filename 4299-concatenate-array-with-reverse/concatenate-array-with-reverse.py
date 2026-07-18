class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        rev = nums [: : -1]
        result = nums+ rev
        return result
            

        
        