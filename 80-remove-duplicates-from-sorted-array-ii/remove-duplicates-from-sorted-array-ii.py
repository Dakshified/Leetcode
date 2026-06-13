class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        start = 1
        for i in range (2, n ):
            if nums[i] != nums [start -1]:
                start = start + 1
                nums[start] = nums[i]
        k = start +1
        return k        
         
        