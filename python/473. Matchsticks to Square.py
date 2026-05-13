from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        side_length = total // 4

        if max(matchsticks) > side_length:
            return False

        # Place longer sticks first to fail faster
        matchsticks.sort(reverse=True)

        sides = [0, 0, 0, 0]

        def backtrack(index: int) -> bool:
            if index == len(matchsticks):
                return (
                    sides[0] == side_length and
                    sides[1] == side_length and
                    sides[2] == side_length and
                    sides[3] == side_length
                )

            stick = matchsticks[index]

            for i in range(4):
                if sides[i] + stick > side_length:
                    continue

                sides[i] += stick

                if backtrack(index + 1):
                    return True

                sides[i] -= stick

                # Optimization:
                # If this stick did not work on an empty side,
                # trying other empty sides is equivalent.
                if sides[i] == 0:
                    break

            return False

        return backtrack(0)