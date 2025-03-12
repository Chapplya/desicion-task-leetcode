class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        '''
        stack = []
        width = 1
        for i in range(len(heights)):
            for j in range(i+1, len(heights)+1):
                if j < len(heights)-1 and heights[i] == heights[j]:
                    width += 1
                else:
                    if not(stack):
                        stack.append(heights[i] * width * width)
                        width = 1
                        break
                    elif stack[-1] <heights[i] * width * width:
                        stack.append(heights[i] * width * width)
                        width = 1
                        break
                    break
        return stack[-1]
    '''
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
                  
        
setting = Solution()        
heights=[7,1,7,2,2,4]

print(setting.largestRectangleArea(heights))
