from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        uglies = [1] * n
        idx = [0] * k
        values = primes[:]   # current candidate for each prime

        for i in range(1, n):
            next_ugly = min(values)
            uglies[i] = next_ugly

            for j in range(k):
                if values[j] == next_ugly:
                    idx[j] += 1
                    values[j] = primes[j] * uglies[idx[j]]

        return uglies[-1]