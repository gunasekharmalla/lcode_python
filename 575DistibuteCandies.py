class Solution(object):
    def distributeCandies(self, candyType):
        n = len(candyType)//2
        n1 = len(set(candyType))
        return min(n,n1)

Input: candyType = [1,1,2,2,3,3]
Output: 3

Input: candyType = [1,1,2,3]
Output: 2
