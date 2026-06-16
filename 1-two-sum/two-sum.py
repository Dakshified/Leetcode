class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range (n):
            for j in range (i +1,n):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    break
        return ans
        

        