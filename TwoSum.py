class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {} #create a dict to store values we visited
        for i in range(len(nums)): # loop through array
            complement = target - nums[i] #get the complement
            if complement in nums_dict: #check if complement exists in
                return [nums_dict[complement],i] #sucess
            nums_dict[nums[i]] = i #add numb to dict

print(Solution().twoSum([2,7,11,15],9))