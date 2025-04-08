
class Solution(object):
    def maxArea(self, height):
        #height = [1,8,6,2,5,4,8,3,7]
        left, right = 0, len(height)-1
        max_area = float('-inf')
        while left < right:
            min_ = min(height[left], height[right])
            width = right - left
            area = min_ * width
            if area > max_area:
                max_area = area
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area

        
