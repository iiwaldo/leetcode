class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        actual_sum = ((len(nums)*(len(nums)+1)) // 2)
        nums_sum = sum(nums)
        return actual_sum - nums_sum 

print(Solution().missingNumber([0,2,3]))