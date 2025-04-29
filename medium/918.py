
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total = 0
        min_sum, max_sum = float('inf'), float('-inf')
        c_min = c_max = 0
        for ele in nums:
            total += ele
            c_max  = max((c_max + ele), ele)
            c_min = min((c_min + ele), ele)
            max_sum = max(max_sum, c_max)
            min_sum = min(min_sum, c_min)
        if max_sum < 0:
            return max_sum
        #res = max(max_sum, total-min_sum)
        return max(max_sum, (total-min_sum))

nums =
[-3,-2,-3]
output: -2
