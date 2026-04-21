class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = {i :[] for i in range(n)}
        for n1,n2 in edges:
            nodes[n1].append(n2)
            nodes[n2].append(n1)
        # print(nodes)
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for i in nodes[node]:
                if i == prev:
                    continue
                
                if not dfs(i,node):
                    return False
            
            return True
        a = dfs(0,-1) 
        # print(visited,a,len(visited),n)
        return a and len(visited)==n
            
            