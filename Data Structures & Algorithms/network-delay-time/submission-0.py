import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))
        # 0 is the weight to get there
        minHeap = [(0,k)]
        heapq.heapify(minHeap)
        visited = set()
        t = 0
        while minHeap:
            currW, currN = heapq.heappop(minHeap)
            if currN in visited:
                continue
            visited.add(currN)
            t = max(t, currW)
            for edgeN, edgeW in edges[currN]:
                if edgeN not in visited:
                    heapq.heappush(minHeap, (currW + edgeW, edgeN))
        return t if len(visited) == n else -1