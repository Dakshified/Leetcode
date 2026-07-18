class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concat = 0
        i = 0
        j = len(nums) - 1
        concat = 0
        while i <= j:
            if i == j:
                concat= concat + nums[i]
            else :
                new = int(str(nums[i]) + str(nums[j]))
                concat = concat + new
            i = i+1
            j = j-1
        return concat
