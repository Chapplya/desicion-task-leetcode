class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums == []:
            return 0
        set_num = set()
        nums = sorted(nums)
        print(nums)
        mas = []
        for i in range(len(nums)):
            if set_num == set():
                set_num.add(nums[i])
                # print(set_num)
                continue
            if nums[i] or nums[i] == 0:
                if nums[i - 1] == nums[i]:
                    continue
                if nums[i - 1] - nums[i] == -1:
                    set_num.add(nums[i])
                    print(set_num)
                else:
                    mas.append(len(set_num))
                    set_num = set()
                    set_num.add(nums[i])
                    continue
            else:
                mas.append(len(set_num))
                return max(mas.append(len(set_num)))
        mas.append(len(set_num))
        return max(mas)


settings = Solution()

nums = [0, 3, 2, 5, 4, 6, 1, 1]
print(nums.sort)
print(settings.longestConsecutive(nums))
