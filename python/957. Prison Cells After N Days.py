from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def next_day(state: List[int]) -> List[int]:
            nxt = [0] * 8
            for i in range(1, 7):
                nxt[i] = 1 if state[i - 1] == state[i + 1] else 0
            return nxt

        seen = {}          # state_tuple -> day_index
        states = []        # states[day_index] = state_tuple
        day = 0
        cur = tuple(cells)

        while day < n and cur not in seen:
            seen[cur] = day
            states.append(cur)
            cur = tuple(next_day(list(cur)))
            day += 1

        if day == n:
            return list(cur)

        # cycle detected: cur is the first repeated state at "day"
        cycle_start = seen[cur]
        cycle_len = day - cycle_start

        # We want the state after n days
        idx = cycle_start + (n - cycle_start) % cycle_len
        return list(states[idx])
