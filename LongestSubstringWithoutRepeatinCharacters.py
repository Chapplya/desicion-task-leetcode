class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            st = set()
            st.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] not in st:
                    st.add(s[j])
                else:
                    break
            res = max(res, len(st))
        return res