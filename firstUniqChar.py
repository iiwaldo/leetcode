class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = {}
        for i in s:
            s_dict[i] = s_dict.get(i,0) + 1
        for i, ch in enumerate(s):
            if s_dict[ch] == 1:
                return i
        return -1
        