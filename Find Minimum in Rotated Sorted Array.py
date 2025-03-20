class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        lf, rt = 0, len(nums) - 1

        while lf <= rt:
            if nums[lf] < nums[rt]:
                res = min(res, nums[lf])
                break


            mid = (lf + rt) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[lf]:
                lf = mid + 1
            else:
                rt = mid - 1
        return res


settings = Solution()

nums = [3, 4, 5, 6, 1, 2]

print(settings.findMin(nums))
