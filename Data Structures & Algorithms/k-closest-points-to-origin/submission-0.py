class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Store a max heap of the relevant size
        pq = []
        heapq.heapify(pq)
        def distance(x,y):
            return (x**2 + y**2)**0.5
        for point in points:
            heapq.heappush(pq, (-1*distance(point[0], point[1]), point))
            if len(pq) > k:
                heapq.heappop(pq)
        
        res = []
        while pq:
            res.append(heapq.heappop(pq)[1])
        return res