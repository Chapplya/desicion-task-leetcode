class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums == []:
            return 0

        set_nums = set(nums)

        longest = 0

        for elem in set_nums:
            if elem - 1 not in set_nums:
                lenght = 1
                while elem + lenght in set_nums:
                    lenght += 1
                longest = max(lenght, longest)
        return longest


settings = Solution()

nums = [-1, 0, 3, 2, 5, 4, 6, 1, 1]

print(settings.longestConsecutive(nums))
