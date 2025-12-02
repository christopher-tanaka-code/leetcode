from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0      # total net gas across all stations
        tank = 0       # current net gas from chosen start
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff

            if tank < 0:
                start = i + 1
                tank = 0

        return start if total >= 0 else -1
