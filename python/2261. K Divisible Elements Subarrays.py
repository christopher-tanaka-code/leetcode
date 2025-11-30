from typing import List

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)

        # Two 64-bit rolling hashes to make collisions extremely unlikely
        B1, B2 = 911382323, 972663749
        MASK = (1 << 64) - 1

        seen = set()

        for i in range(n):
            div_cnt = 0
            h1 = 0
            h2 = 0
            for j in range(i, n):
                if nums[j] % p == 0:
                    div_cnt += 1
                    if div_cnt > k:
                        break

                x = nums[j] + 1  # shift to avoid zeros interacting with hashing
                h1 = (h1 * B1 + x) & MASK
                h2 = (h2 * B2 + x) & MASK

                # include length to be extra-safe
                seen.add((h1, h2, j - i + 1))

        return len(seen)
