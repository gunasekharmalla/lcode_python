class Solution(object):
    def findDuplicate(self, nums):
        freq = {}
        for ele in nums:
            freq[ele] = freq.get(ele, 0) + 1
        for key, val in freq.items():
            if val > 1:
                return key

nums = [1,3,4,2,2]
output = 2
