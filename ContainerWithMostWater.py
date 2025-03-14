class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        mxar = 0
        while left < right:
            res = (right - left) * min(height[left], height[right])
            mxar = max(mxar, res)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return mxar


settings = Solution()

height = [1,7,2,5,4,7,3,6]

print(settings.maxArea(height))
