class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for i in s:
            if i not in s_dict:
                s_dict[i] = 1
            else:
                s_dict[i] = s_dict[i] + 1
        
        for i in t:
            if i not in t_dict:
                t_dict[i] = 1
            else:
                t_dict[i] = t_dict[i] + 1
                
        if s_dict != t_dict:
            return False
        return True
        