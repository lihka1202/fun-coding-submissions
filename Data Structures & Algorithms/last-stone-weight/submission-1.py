class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-1*stone for stone in stones]
        heapq.heapify(pq)
        while len(pq) > 1:
            s1 = -1*heapq.heappop(pq)
            s2 = -1*heapq.heappop(pq)
            heapq.heappush(pq, -1*(s1-s2)) if s1-s2 > 0 else print("whoops")
        if pq:
            return -1 * pq[0]
        else:
            return 0