class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1]* (len(edges)+1)
        def find(n):
            if parent[n] == n:
                return n
            parent[n] = find(parent[n])
            return parent[n]
        def unionFind(n1,n2):
            n1,n2 = find(n1),find(n2)
            if n1 == n2:
                return False
            
            if rank[n1]> rank[n2]:
                parent[n2] = n1
                rank[n1] +=rank[n2]
            else:
                parent[n1] =n2
                rank[n2] +=rank[n1]

            return True

        for n1,n2 in edges:
            if not unionFind(n1,n2):
                return [n1,n2]
