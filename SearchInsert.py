class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start_pointer = 0
        end_pointer = len(nums) -1
        while start_pointer <= end_pointer:
            middle = (start_pointer + end_pointer) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                start_pointer = middle+1
                middle = (start_pointer + end_pointer) // 2
            if nums[middle] > target:
                end_pointer = middle-1
                middle = (start_pointer + end_pointer) // 2
        return start_pointer