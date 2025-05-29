class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        op = set(['*','+','-','/'])
        stack = []
        for val in tokens:
            if val == "+":
                stack.append(stack.pop()+stack.pop())
            elif val == '-':
                num_2 , num_1 = stack.pop(), stack.pop()
                stack.append(num_1-num_2)
            elif val == "*":
                stack.append(stack.pop()*stack.pop())
            elif val == "/":
                num_2 , num_1 = stack.pop(), stack.pop()
                stack.append(int(float(num_1)/num_2))
            else:
                stack.append(int(val))
        return stack.pop()