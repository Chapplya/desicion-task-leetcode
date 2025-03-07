class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        elem_ = {'+', '-', '*', '/'}
        if tokens[0] in elem_: return False
        for i in range(len(tokens)):
            if tokens[i] not in elem_:
                stack.append(int(tokens[i]))
            else:
                if tokens[i] == '+':
                    stack.append(stack[-2]+stack[-1])
                elif tokens[i] == '-':
                    stack.append(stack[-2]-stack[-1])
                elif tokens[i] == '*':
                    stack.append(stack[-2]*stack[-1])
                elif tokens[i] == '/':
                    stack.append(int(stack[-2]/stack[-1]))
        
        return stack[-1]

settings = Solution()

tokens = ["1","2","+","3","*","4","-"]

print(settings.evalRPN(tokens))
                
                
                