class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True

        stack = []
        brackets = {")": "(", "}": "{", "]": "["}

        for elem in s:
            if elem in brackets:
                if stack and stack[-1] != brackets[elem]:
                    return False
                stack.pop()
            else:
                stack.append(elem)
        return stack == []


settings = Solution()

s = "[][][][]"

assert settings.isValid("())")
assert settings.isValid(s)
