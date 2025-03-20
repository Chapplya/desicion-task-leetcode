import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lf, rr = 1, max(piles)
        res = rr

        while lf <= rr:
            kr = (lf + rr) // 2

            totalTime = 0
            for elem in piles:
                totalTime += math.ceil(float(elem) / kr)
            if totalTime <= h:
                res = kr
                rr = kr - 1
            else:
                lf = kr + 1
        return res


sett = Solution()
piles = [25, 10, 23, 4]
h = 4

print(sett.minEatingSpeed(piles, h))
