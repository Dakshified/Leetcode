class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        sums.append(nums[0])
        n = len(nums)
        for i in range (1,n):
            x = sums[i-1] + nums [i]
            sums.append(x)
        return sums 
