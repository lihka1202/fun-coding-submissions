class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgeList = {}
        for start,end in edges:  
            if end not in edgeList:
                edgeList[end] = []
            if start not in edgeList:
                edgeList[start] = []
            edgeList[start].append(end)
            edgeList[end].append(start)
        print(edgeList)
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            if node in edgeList:
                for end in edgeList[node]:
                    dfs(end)
        count = 0
        for i in range(n):
            if i not in visited:
                print(i)
                dfs(i)
                count += 1
        return count
