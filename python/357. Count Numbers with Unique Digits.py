class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        total = 10
        current = 9
        available_digits = 9

        for length in range(2, n + 1):
            current *= available_digits
            total += current
            available_digits -= 1

        return total