class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        final = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            a = nums[i]
            left, right = i+1, len(nums)-1

            while left < right:
                res = a + nums[left] + nums[right]
                if res < 0:
                    left += 1
                elif res > 0:
                    right -= 1
                else:
                    final.append([a, nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return final
        
