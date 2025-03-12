class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target and numbers[i] != numbers[j]:
                    return [i+1,j+1]
        return []



settings = Solution()

numbers = [6,8,1,2]
target = 3

print(settings.twoSum(numbers,target))