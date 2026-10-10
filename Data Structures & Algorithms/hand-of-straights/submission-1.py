class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        no_groups = len(hand) // groupSize

        # build the result
        res = [[] for _ in range(no_groups)]

        hand.sort()

        for n in hand:
            # Check if each number got placed
            placed = False
            for counter in range(no_groups):
                # Iter through the groups and see best fit
                if res[counter] == []:
                    # Empty, append
                    res[counter].append(n)
                    placed = True
                    break
                elif (n - res[counter][-1]) == 1 and len(res[counter]) < groupSize:
                    # Got space, append
                    res[counter].append(n)
                    placed = True
                    break
                else:
                    continue
            if not placed:
                return False
        return True