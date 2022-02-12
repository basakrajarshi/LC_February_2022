class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0
        
        left = 0
        right = len(height)-1
        max_area = 0
        area = 0
        
        while left != right:
            area = min(height[left], height[right])*(right - left)
            max_area = max(max_area, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
            
