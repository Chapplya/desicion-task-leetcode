import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        speed = 1
        while True:
            avgtime = 0
            for elem in piles:
                avgtime = math.ceil(elem / speed)
            if avgtime <= h:
                return speed
            else:
                speed += 1


sett = Solution()
piles = [25, 10, 23, 4]
h = 4

print(sett.minEatingSpeed(piles, h))
