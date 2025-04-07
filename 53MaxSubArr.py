class Solution(object):
    def maxSubArray(self, nums):
        max_ending = max_sum = nums[0]
        for left in range(1,len(nums)):
            max_ending = max(nums[left], (max_ending+nums[left]))
            max_sum = max(max_sum, max_ending)
        return max_sum
        
