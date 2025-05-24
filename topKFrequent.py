class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        freq = [[] for _ in range(len(nums)+1)]
        for key , value in count.items():
            freq[value].append(key)
        res = []
        for i in range(len(freq) -1,0,-1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    return res