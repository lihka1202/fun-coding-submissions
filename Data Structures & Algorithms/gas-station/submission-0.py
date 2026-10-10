class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        if len(gas) == 1:
            return 0
        mi = -1
        maxgas = 0
        for i in range(len(cost)):
            # never been touched before
            if maxgas ==  0 and (gas[i] - cost[i]) + maxgas > 0:
                mi = i
                maxgas = (gas[i] - cost[i]) + maxgas
            elif (gas[i] - cost[i]) + maxgas < 0:
                maxgas = 0
                mi = -1
            else:
                maxgas += (gas[i] - cost[i])
            print(gas[i] - cost[i], maxgas)
        print(maxgas)
        print(mi)
        return mi