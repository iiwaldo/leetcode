class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paratheses_dict = {')':'(','}':'{',']':'['}
        stack = []
        for char in s:
            if char in paratheses_dict:
                if not stack or stack.pop() != paratheses_dict[char]:
                    return False
                else:
                    continue
            stack.append(char)
        return not stack
        