from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        count = Counter(nums)
        cnts = dict(count)
        mx = max(cnts,key = cnts.get)
        val = cnts[mx]
        return mx   
        