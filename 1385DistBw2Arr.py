
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        set1 = {}
        for val in range(len(nums)):
            if nums[val] in set1 and abs(val - set1[nums[val]]) <= k:
                return True 
            set1[nums[val]] = val
        return False


Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2

Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1
