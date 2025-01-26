
class Solution(object):
    def countPartitions(self, nums):
        c = 0
        for i in range(1, len(nums)):
            ls1 = nums[:i]
            ls2 = nums[i:]
            s1 = sum(ls1)
            s2 = sum(ls2)
            if (s1 - s2) % 2 == 0:
                c += 1
        return c
         
