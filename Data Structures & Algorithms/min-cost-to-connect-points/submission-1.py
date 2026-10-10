class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Generally the basic idea is to build a min spanning tree, and the idea is to use either prims 
        # or kruskals
        if len(points) == 1:
            return 0
        edgeList = {}
        counterSet = set()
        # Build the adjacency list
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                if (points[i][0], points[i][1]) not in edgeList:
                    edgeList[(points[i][0], points[i][1])] = []
                if (points[j][0], points[j][1]) not in edgeList:
                    edgeList[(points[j][0], points[j][1])] = []
                edgeList[(points[i][0], points[i][1])].append((distance, (points[j][0], points[j][1])))
                edgeList[(points[j][0], points[j][1])].append((distance, (points[i][0], points[i][1])))
        minHeap = [(0, (points[0][0], points[0][1]))]
        heapq.heapify(minHeap)
        finalDistance = 0
        print(edgeList)

        while len(counterSet) != len(points) and len(minHeap) > 0:
            # pop
            distance, point = heapq.heappop(minHeap)
            print("Distance: ",distance)
            print("Point: ",point)
            if point not in counterSet:
                finalDistance += distance
                counterSet.add(point)
                # Iterate through its neighbours
                for element in edgeList[point]:
                    heapq.heappush(minHeap, element)
        return finalDistance
                    

