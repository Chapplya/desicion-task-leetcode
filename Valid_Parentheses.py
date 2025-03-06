class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        clos_opn = {")": "(", "}": "{", "]": "["}
        for elem in s:
            if elem in clos_opn:
                if stack and stack[-1] == clos_opn[elem]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(elem)
        return True if stack == [] else False


settings = Solution()

s = "[][][][]"

assert settings.isValid(s)
