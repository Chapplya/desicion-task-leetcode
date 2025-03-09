class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        elem_ = {"+", "-", "*", "/"}
        if tokens[0] in elem_:
            return False
        for i in range(len(tokens)):
            if tokens[i] not in elem_:
                stack.append(int(tokens[i]))
            else:
                if tokens[i] == "+":
                    stack.append(stack.pop() + stack.pop())
                elif tokens[i] == "-":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                elif tokens[i] == "*":
                    stack.append(stack.pop() * stack.pop())
                elif tokens[i] == "/":
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(float(b) / a))
        return stack[0]


settings = Solution()

tokens = ["1", "2", "+", "3", "*", "4", "-"]

print(settings.evalRPN(tokens))
