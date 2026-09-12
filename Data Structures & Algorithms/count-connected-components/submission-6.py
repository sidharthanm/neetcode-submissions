class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edged = {}
        if not edges:
            return n
        # for x in edges:
            # print(x)
        for x in edges:
            # print(edges,x)
            i = int(x[0])
            v = int(x[1] )
            if i not in edged:
                edged[i] = [v,]
            else:
                edged[i].append(v)
            
            if v not in edged:
                edged[v]= [i,]
            else:
                edged[v].append(i)
        
        visited = set()
        res  = 0
        def dfs(node):
            # if node in visited:            

            for i in edged[node]:
                if i in visited:
                    continue
                visited.add(i)
                dfs(i)
            
        for i in range(n):
            # print(visited)
            if i in visited:
                continue
            if i not in edged:
                visited.add(i)
            else:
                dfs(i)
            res+=1
        
        return res
                

