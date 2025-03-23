class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        lenght = len(nums1) + len(nums2)
        merg_list = nums1 + nums2
        merg_list.sort()

        if lenght % 2 == 0:
            return (merg_list[lenght//2 - 1] +  merg_list[lenght//2])/2
        else:
            return merg_list[lenght//2 ]
        
    
settings = Solution()
        
nums1 = [1,3]
nums2 = [2,4]

print(settings.findMedianSortedArrays(nums1,nums2))

