class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Basically start thinking about how to approach this
        # Since we're constrained by the number of jumps to make, perhaps a good idea to use Bellman Ford
        dv = [float("inf")] * n 
        dv[src] = 0
        # The distance from the source to itself is always 0

        for _ in range(k + 1):
            tempDv = dv.copy()
            for start, end, distance in flights:
                # 2 main conditions
                # If the current source is infinity, then there is no current path that can be seen to it
                if tempDv[start] == float("inf"):
                    continue
                
                # Check if we can minimize the total distance so far this current point based on the edge length
                tempDv[end] = min(tempDv[end], dv[start] + distance)
            dv = tempDv
        return dv[dst] if dv[dst] != float("inf") else -1