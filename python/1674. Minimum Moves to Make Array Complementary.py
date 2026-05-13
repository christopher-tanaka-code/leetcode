from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        # Possible target sums are from 2 to 2 * limit.
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            current_sum = a + b

            # Default cost for each pair is 2 moves.
            diff[2] += 2

            # Target sums in [low, high] can be achieved in 1 move.
            diff[low] -= 1
            diff[high + 1] += 1

            # Target sum equal to current_sum needs 0 moves.
            diff[current_sum] -= 1
            diff[current_sum + 1] += 1

        answer = float("inf")
        moves = 0

        for target_sum in range(2, 2 * limit + 1):
            moves += diff[target_sum]
            answer = min(answer, moves)

        return answer