class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        '''
        First solution 
        count = 0
        mas = []
        for i in range(len(position)):
            for j in range(i, len(position)): 
                if (target - position[i])/speed[i] != (target - position[j])/speed[j] and j not in mas:
                    count += 1
                else:
                    mas.append(j)
                print(count)
                print(mas)
        return count
        '''
        
        lst = [(pos, spd) for pos, spd in zip(position, speed)]
        stack = []
        lst.sort(reverse=True)
        for pos, spd in lst:
            stack.append((target - pos)/ spd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    
settings = Solution()

target=12
position=[10,8,0,5,3]
speed=[2,4,1,1,3]

print(settings.carFleet(target, position, speed))