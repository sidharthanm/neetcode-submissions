class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        ROWS,COLS = len(heights),len(heights[0])
        pacific = set()
        atlantic = set()
        direction = ((1,0),(0,1),(-1,0),(0,-1))
        
        
        def flood(r,c,v,p):
            if (r,c) in v or r< 0 or c<0 or r == ROWS or c == COLS or heights[r][c] < p:
                return
            
            v.add((r,c))
            for i,j in direction:
                flood(r+i,c+j,v,heights[r][c])
        
        for c in range(COLS):
            flood(0,c,pacific,heights[0][c])
            flood(ROWS-1,c,atlantic,heights[ROWS-1][c])
        
        for r in range(ROWS):
            flood(r,0,pacific,heights[r][0])
            flood(r,COLS -1,atlantic,heights[r][COLS -1 ])
        
        res =[]

        for i in pacific:
            if i in atlantic:
                res.append(list(i))
        
        return res
            

            
