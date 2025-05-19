class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uni_dict = {}
        for i in nums:
            if i == 0:
                continue
            elif i not in uni_dict:
                uni_dict[i] = True
        return len(uni_dict)
