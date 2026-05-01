class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_length = 1
        count = 9
        start = 1

        # Find the block where the nth digit belongs.
        # 1-digit numbers: 1 to 9        -> 9 * 1 digits
        # 2-digit numbers: 10 to 99      -> 90 * 2 digits
        # 3-digit numbers: 100 to 999    -> 900 * 3 digits
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10

        # Find the actual number containing the nth digit.
        number = start + (n - 1) // digit_length

        # Find the digit index inside that number.
        digit_index = (n - 1) % digit_length

        return int(str(number)[digit_index])