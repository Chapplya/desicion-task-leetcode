class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alph = ''
        for elem in s:
            if 97 <= ord(elem) <= 122 or 48 <= ord(elem) <=57 or 65 <= ord(elem) <= 90: 
                s_alph += elem
        s_alph = s_alph.lower()
        print(s_alph)
        j = len(s_alph)-1
        
        for i in range(len(s_alph)//2):
            if s_alph[i] != s_alph[j-i]:
                return False
        return True
            
 
settings = Solution()       
s = "A man, a plan, a canal: Panama"

print(settings.isPalindrome(s))