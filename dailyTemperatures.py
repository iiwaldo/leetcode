class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # [4,3,2,7]
        stack = []
        res = [0]*len(temperatures)
        for i,v in enumerate(temperatures):
            while stack and v > temperatures[stack[-1]]:
                index = stack.pop()
                res[index]= i-index
            stack.append(i)
        return res