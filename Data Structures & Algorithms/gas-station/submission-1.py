class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = sum(gas) - sum(cost)
        if total_tank < 0:
            return -1

        curr_tank = 0
        start_index = 0

        for i in range(len(gas)):
            curr_tank += gas[i]
            curr_tank = curr_tank - cost[i]

            if curr_tank < 0:
                curr_tank = 0
                start_index = i + 1
            
        return start_index