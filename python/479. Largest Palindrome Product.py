class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9

        upper = 10 ** n - 1
        lower = 10 ** (n - 1)

        for left in range(upper, lower - 1, -1):
            p = int(str(left) + str(left)[::-1])

            x = upper
            while x * x >= p:
                if p % x == 0:
                    y = p // x
                    if lower <= y <= upper:
                        return p % 1337
                x -= 1

        return -1