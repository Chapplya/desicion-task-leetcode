class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alph = ''
        for elem in s:
            if elem.isalnum():
                s_alph += elem.lower()
        return s_alph == s_alph[::-1]
 
settings = Solution()       
s = "A man, a plan, a canal: Panama"

print(settings.isPalindrome(s))