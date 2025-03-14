class Solution(object):
    def maxArea(self, height):
        mxar = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                mxar = max(mxar, (j - i) * min(height[i], height[j]))
        return mxar


settings = Solution()

height = [1, 7, 2, 5, 4, 7, 3, 6]

print(settings.maxArea(height))
