class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)*len(matrix[0])

        while l<=r:
            cur  = l+((r-l)//2)
            row = cur//len(matrix)-1 if cur//len(matrix)-1 >=0 else 0 
            col = cur%len(matrix[0])-1 if cur%len(matrix[0])-1 >=0 else 0
            print(l,r,cur,row,col)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] <target:
                l = cur+1
            else:
                r = cur-1
        
        return False

             