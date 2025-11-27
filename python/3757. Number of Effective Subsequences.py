from typing import List

class Solution:
    def countEffective(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Total OR (strength)
        T = 0
        for x in nums:
            T |= x
        if T == 0:  # (not possible with given constraints, but kept for completeness)
            return 0

        # Compress the bits that appear in T into [0..m-1]
        bit_pos = [b for b in range(21) if (T >> b) & 1]  # nums[i] <= 1e6 < 2^20
        m = len(bit_pos)
        ALL = (1 << m) - 1
        idx = {b: i for i, b in enumerate(bit_pos)}  # original bit -> compressed index

        # f[mask] = how many nums have exactly this pattern of bits (restricted to bits in T)
        f = [0] * (1 << m)
        for x in nums:
            y = x & T
            mask = 0
            while y:
                lsb = y & -y
                b = lsb.bit_length() - 1
                mask |= 1 << idx[b]
                y -= lsb
            f[mask] += 1

        # SOS DP: g[mask] = sum_{sub ⊆ mask} f[sub]
        # i.e., count of elements whose bitmask is a subset of 'mask'
        g = f[:]
        for i in range(m):
            bit = 1 << i
            for mask in range(1 << m):
                if mask & bit:
                    g[mask] += g[mask ^ bit]

        # powers of 2 up to n
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        # Count "ineffective" removals: remaining OR stays T
        # Inclusion-exclusion over bits of T:
        # For subset B of bits, let none(B) = count of elements with no bits from B.
        # Then #removals that must include all elements having any bit in B is 2^{none(B)}.
        ineffective = 0
        for B in range(1 << m):
            none_cnt = g[ALL ^ B]          # masks with (mask & B) == 0 are subsets of complement
            ways = pow2[none_cnt]          # 2^(n - |union|) = 2^none_cnt
            if B.bit_count() & 1:
                ineffective = (ineffective - ways) % MOD
            else:
                ineffective = (ineffective + ways) % MOD

        total = pow2[n]
        effective = (total - ineffective) % MOD
        return effective
