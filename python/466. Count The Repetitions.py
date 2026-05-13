class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0

        # If s2 contains a character not in s1, it can never be formed.
        if not set(s2).issubset(set(s1)):
            return 0

        index_s2 = 0
        count_s2 = 0

        # seen[index_s2] = (s1_blocks_used, s2_count_formed)
        seen = {}

        s1_blocks = 0

        while s1_blocks < n1:
            s1_blocks += 1

            for ch in s1:
                if ch == s2[index_s2]:
                    index_s2 += 1

                    if index_s2 == len(s2):
                        index_s2 = 0
                        count_s2 += 1

            # If we have seen this same s2 position before,
            # the process will repeat in a cycle.
            if index_s2 in seen:
                prev_s1_blocks, prev_count_s2 = seen[index_s2]

                cycle_s1_blocks = s1_blocks - prev_s1_blocks
                cycle_s2_count = count_s2 - prev_count_s2

                remaining_s1_blocks = n1 - s1_blocks
                cycles = remaining_s1_blocks // cycle_s1_blocks

                s1_blocks += cycles * cycle_s1_blocks
                count_s2 += cycles * cycle_s2_count

                # Clear seen to avoid applying cycle skip repeatedly.
                seen.clear()
            else:
                seen[index_s2] = (s1_blocks, count_s2)

        return count_s2 // n2