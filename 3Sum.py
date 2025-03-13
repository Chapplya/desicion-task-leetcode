class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sor_nums = sorted(nums)
        backet = []

        for i in range(len(sor_nums)):
            if sor_nums[i] > 0:
                break

            if i > 0 and sor_nums[i] == sor_nums[i - 1]:
                continue

            left = i + 1
            right = len(sor_nums) - 1
            while left < right:
                summ = sor_nums[i] + sor_nums[left] + sor_nums[right]

                if summ < 0:
                    left += 1
                elif summ > 0:
                    right -= 1
                else:
                    backet.append([sor_nums[i], sor_nums[left], sor_nums[right]])
                    left += 1
                    right -= 1
                    while left < right and sor_nums[left] == sor_nums[left - 1]:
                        left += 1

        return backet


settings = Solution()

nums = [5, 0, 1, 2, -1, -4]

print(settings.threeSum(nums))
