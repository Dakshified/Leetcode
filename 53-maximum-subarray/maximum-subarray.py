class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]
        curr_sum = 0
        for i in range (0,n):
            curr_sum = nums[i] + curr_sum
            if curr_sum > max_sum :
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_sum