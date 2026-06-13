class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        n = len(nums)
        for i in range (1,n):
            if nums[i] != nums[start] :
                start = start + 1
                nums[start] = nums [i]
        k = start + 1
        return k 