class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_mul = 1
        right_mul = 1
        left = []
        right = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            left_mul = left_mul * nums[i]
            left.append(left_mul)
        for i in range(len(nums)-1,-1,-1):
            right_mul = right_mul * nums[i]
            right[i] = right_mul
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(right[i+1])
            elif i == len(nums)-1:
                res.append(left[i-1])
            else:
                res.append(left[i-1]*right[i+1])
        return res
        