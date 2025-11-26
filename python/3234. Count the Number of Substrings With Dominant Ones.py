from typing import List
import math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zeros = [i for i, ch in enumerate(s) if ch == '0']
        m = len(zeros)

        zmax = int(math.isqrt(n))  # max possible zeros in a valid substring
        offset = [0] * (zmax + 1)  # offset[z] = z*z + z - 1
        for z in range(1, zmax + 1):
            offset[z] = z * z + z - 1

        ans = 0
        k = 0  # first zero index in `zeros` that is >= i

        for i in range(n):
            if i > 0 and s[i - 1] == '0':
                k += 1

            # z = 0: substrings with no zeros (all ones)
            first_zero = zeros[k] if k < m else n
            ans += first_zero - i

            # z >= 1
            for z in range(1, zmax + 1):
                need_end = i + offset[z]
                if need_end >= n:
                    break

                idx_last = k + z - 1
                if idx_last >= m:
                    break

                last_zero = zeros[idx_last]
                next_zero = zeros[idx_last + 1] if idx_last + 1 < m else n

                start_end = last_zero if last_zero > need_end else need_end
                if start_end < next_zero:
                    ans += next_zero - start_end

        return ans
