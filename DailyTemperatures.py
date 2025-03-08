class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = []
        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    res.append(j-i)
                    break
                if j == len(temperatures)-1:
                    res.append(0)

        return res
        
settings = Solution()

temperatures = [30,38,30,36,35,40,28]   

print(settings.dailyTemperatures(temperatures))
