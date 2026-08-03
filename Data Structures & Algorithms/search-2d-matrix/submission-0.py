class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)*len(matrix[0])

        while l<=r:
            cur  = l+(r-l)//2
            row = cur//len(matrix)
            col = cur%len(matrix[0])

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] <target:
                l = cur+1
            else:
                r = cur-1
        
        return False

             