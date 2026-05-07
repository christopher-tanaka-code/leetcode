from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i: int) -> int:
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            direction = nums[i] > 0
            slow = fast = i

            while True:
                # Move slow one step
                next_slow = next_index(slow)

                if nums[next_slow] == 0 or (nums[next_slow] > 0) != direction:
                    break

                # Self-loop is invalid because cycle length must be > 1
                if next_slow == slow:
                    break

                # Move fast one step
                next_fast = next_index(fast)

                if nums[next_fast] == 0 or (nums[next_fast] > 0) != direction:
                    break

                if next_fast == fast:
                    break

                # Move fast second step
                next_fast2 = next_index(next_fast)

                if nums[next_fast2] == 0 or (nums[next_fast2] > 0) != direction:
                    break

                if next_fast2 == next_fast:
                    break

                slow = next_slow
                fast = next_fast2

                if slow == fast:
                    return True

            # Mark this path as visited so we do not process it again
            current = i
            while nums[current] != 0 and (nums[current] > 0) == direction:
                nxt = next_index(current)

                # Mark current as visited
                nums[current] = 0

                current = nxt

        return False