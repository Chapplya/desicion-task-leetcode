class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2 #  привычка из плюсов, чтобы переполнения типов не было 
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
                
        return nums[left]


settings = Solution()

nums = [3, 4, 5, 6, 1]

print(settings.findMin(nums))
