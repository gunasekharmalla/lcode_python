class Solution(object):
    def sortColors(self, nums):
        left,right = 0, len(nums)-1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                i += 1
                left += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
          
            else:
                i += 1
  
        return nums
        
nums = [2,0,2,1,1,0]
result = [0,0,1,1,2,2]
