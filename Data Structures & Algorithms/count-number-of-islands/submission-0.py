class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res =0
        visited = set()
        directions = ((-1,0),(1,0),(0,1),(0,-1))
        def flood(r,c):
            if (r,c) in visited:
                return
            
            if grid[r][c] == "0":
                return

            

            visited.add((r,c))
            grid[r][c] = "0"

            for i,j in directions:
                if 0<=r+i<len(grid) and 0<=c+j < len(grid[0]):
                    
                    flood(r+i,c+j)
            
            return


        total = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] =="1":
                    res+=1
                    flood(row,column)
        
        return res
        