class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        left = 0
        right = len(numbers)-1
        while left < right:
            summ = numbers[left] + numbers[right]
            if summ > target:
                right -= 1
            elif summ < target:
                left += 1
            else:
                return [left + 1, right + 1]
        return []


settings = Solution()

numbers = [6,8,1,2]
target = 3

print(settings.twoSum(numbers,target))