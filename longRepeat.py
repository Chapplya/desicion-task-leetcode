
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        aphset = set(s)
        res = 0
        for elem in aphset:
            left = 0
            cnt = 0
            for right in range(len(s)):
                if s[right] == elem:
                    cnt += 1
                while (right - left + 1) - cnt > k:
                    if s[left] == elem:
                        cnt -= 1
                    left += 1 

                res = max(res, right - left + 1)
        return res
