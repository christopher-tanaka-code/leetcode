from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        digit_count = [0] * 10

        # Unique identifying letters
        digit_count[0] = count["z"]  # zero
        digit_count[2] = count["w"]  # two
        digit_count[4] = count["u"]  # four
        digit_count[6] = count["x"]  # six
        digit_count[8] = count["g"]  # eight

        # Remaining digits after removing unique ones
        digit_count[3] = count["h"] - digit_count[8]  # three, eight
        digit_count[5] = count["f"] - digit_count[4]  # five, four
        digit_count[7] = count["s"] - digit_count[6]  # seven, six

        digit_count[1] = count["o"] - digit_count[0] - digit_count[2] - digit_count[4]  # one, zero, two, four
        digit_count[9] = count["i"] - digit_count[5] - digit_count[6] - digit_count[8]  # nine, five, six, eight

        result = []

        for digit in range(10):
            result.append(str(digit) * digit_count[digit])

        return "".join(result)