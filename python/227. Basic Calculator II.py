class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        last = 0
        result = 0
        op = "+"

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + ord(ch) - ord("0")

            if ch in "+-*/" or i == len(s) - 1:
                if op == "+":
                    result += last
                    last = num
                elif op == "-":
                    result += last
                    last = -num
                elif op == "*":
                    last *= num
                else:  # op == "/"
                    last = int(last / num)  # truncates toward zero

                op = ch
                num = 0

        return result + last
