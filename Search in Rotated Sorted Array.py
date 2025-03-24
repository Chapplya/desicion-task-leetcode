class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lf, rt = 0, len(nums) - 1

        while lf <= rt:
            mid = (lf + rt) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[lf] :
                
                if target > nums[mid] or target < nums[lf]:
                    lf = mid + 1
                else:
                    rt = mid - 1
                
                
            else:
                if target < nums[mid] or target > nums[rt]:
                    rt = mid - 1
                else:
                    lf = mid + 1
        return -1

settings = Solution()

nums=[4,5,6,7,0,1,2]
target=0
print(settings.search(nums, target))