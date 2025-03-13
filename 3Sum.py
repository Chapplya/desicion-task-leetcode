class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sor_nums = sorted(nums)
        backet = []

        for i in range(len(sor_nums)):
            if sor_nums[i] > 0:
                break

            if i > 0 and sor_nums[i] == sor_nums[i - 1]:
                continue

            l = i + 1
            r = len(sor_nums) - 1
            while l < r:
                summ = sor_nums[i] + sor_nums[l] + sor_nums[r]

                if summ < 0:
                    l += 1
                elif summ > 0:
                    r -= 1
                else:
                    backet.append([sor_nums[i], sor_nums[l], sor_nums[r]])
                    l += 1
                    r -= 1
                    while sor_nums[l] == sor_nums[l - 1] and l < r:
                        l += 1
        return backet


settings = Solution()

nums = [5, 0, 1, 2, -1, -4]

print(settings.threeSum(nums))
