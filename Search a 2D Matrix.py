class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]: 
            return False
        i = 0
        while i <= len(matrix)-1:
            if matrix[i][0] <= target <= matrix[i][-1]:
                if target == matrix[i][0] or target == matrix[i][-1]:
                    return True
                else:
                    left = 0
                    right = len(matrix[0])-1
                    while left <= right:
                        mid = (left + right)//2
                        if matrix[i][mid] == target:
                            return True
                        elif matrix[i][mid] < target:
                            left = mid + 1
                        else:
                            right = mid - 1
                    return False
            else:
                i += 1
        return  False

sol = Solution()

matrix = [[-8,-7,-5,-3,-3,-1,1],[2,2,2,3,3,5,7],[8,9,11,11,13,15,17],[18,18,18,20,20,20,21],[23,24,26,26,26,27,27],[28,29,29,30,32,32,34]]

target = -5

print (sol.searchMatrix(matrix, target))



                        
            