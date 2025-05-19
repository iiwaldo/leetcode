class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for word in strs:
            count = [0] * 26 #a-z
            for char in word:
                count[ord(char)-ord('a')] += 1
            if tuple(count) in res:
                res[tuple(count)].append(word)
            else:
                res[tuple(count)] = [word]
        res = list(res.values())
        return res

            
        