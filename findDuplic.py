class Solution:
    def findDuplicate(self, nums) -> int:
        for el in nums:
            idx = abs(el) - 1
            if nums[idx] < 0:
                return abs(el)
            nums[idx] *= -1
