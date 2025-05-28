class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l , r = 0, len(height) - 1
        max_l, max_r = height[l],height[r]
        count = 0
        while l < r:
            if max_l < max_r:
                l+=1
                max_l = max(max_l,height[l])
                count += max_l - height[l]
            else:
                r-=1
                max_r = max(max_r,height[r])
                count += max_r - height[r]
        return count

            