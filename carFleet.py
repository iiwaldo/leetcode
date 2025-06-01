class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        #t = d/s
        ps = sorted(zip(position,speed), reverse=True)
        stack = []
        for pos,sp in ps:
            t = (target-pos)/sp 
            if stack and t <= stack[-1]:
                continue
            stack.append(t)
        return len(stack)


