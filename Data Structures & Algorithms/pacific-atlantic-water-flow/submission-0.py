class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        reach = set()
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        
        PACIFIC = []
        for i in range(len(heights[0])):
            pacific.append((0,i))
            
        
        def flood(r,c):
            if (r,c) in set:
                return True
            

            
