class Solution(object):
    def sortedSquares(self, nums):
        res = [x**2 for x in nums]
        res.sort()
        return res
        
