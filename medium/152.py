class Solution(object):
    def maxProduct(self, nums):
        res = max(nums) 
        cur_max, cur_min = 1, 1
        for ele in nums:
            if ele == 0:
                cur_max, cur_min = 1, 1
                continue
            temp = cur_max * ele
            cur_max = max(ele, temp, cur_min * ele)
            cur_min = min(ele, temp, cur_min * ele)
            res = max(res, cur_max)
        return res

