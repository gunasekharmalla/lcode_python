class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        #nums.sort()
        ls=[]
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    continue
                else:
                    if nums[i] > nums[j]:
                        cnt +=1
            ls.append(cnt)
        return ls
      
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
