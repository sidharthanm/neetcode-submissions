class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = { i : i for i in range(n)}
        revparent = {i : i for i in range(n)} 
        
        res = n
        for n1,n2 in edges:
            if parent[n2]!= parent[n1]:
                res -=1 
                parent[n2] = parent[n1]
                
        
        # print(parent,res)
        # return len(set(parent.values()))
        return res        
