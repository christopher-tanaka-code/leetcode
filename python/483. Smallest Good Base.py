class Solution:
    def smallestGoodBase(self, n: str) -> str:
        N = int(n)

        def value(base: int, length: int) -> int:
            total = 1
            cur = 1
            for _ in range(1, length):
                cur *= base
                total += cur
                if total > N:
                    break
            return total

        for length in range(N.bit_length(), 2, -1):
            left, right = 2, int(N ** (1 / (length - 1))) + 2

            while left <= right:
                mid = (left + right) // 2
                total = value(mid, length)

                if total == N:
                    return str(mid)
                elif total < N:
                    left = mid + 1
                else:
                    right = mid - 1

        return str(N - 1)