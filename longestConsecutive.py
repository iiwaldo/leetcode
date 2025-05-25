class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        max_length = 1
        for num in nums_set:
            if num-1 not in nums_set:
                output = 1
                current = num
                while current+1 in nums_set:
                    output+=1
                    current = current+1
                if output > max_length:
                    max_length = output
        return max_length
