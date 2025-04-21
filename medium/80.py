class Solution(object):
    def removeDuplicates(self, nums):
        j, i, cnt = 0, 1, 0
        while i < len(nums):
            if nums[i] == nums[j] and cnt == 0:
                j += 1
                nums[j] = nums[i]
                cnt += 1
                i += 1
            elif nums[i] == nums[j] and cnt > 0:
                i += 1
            else:
                j += 1
                nums[j] = nums[i]
                cnt = 0
                i += 1
        return j + 1

