class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        m = 0
        while l < r:
            m = max(m, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l+=1
            elif height[l] > height[r]:
                r-=1
            else:
                l+=1
                r-=1
        return m
        