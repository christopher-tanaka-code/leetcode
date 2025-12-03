class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        num = 0
        sign = 1
        stack = []

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)

            elif c == '+':
                result += sign * num
                num = 0
                sign = 1

            elif c == '-':
                result += sign * num
                num = 0
                sign = -1

            elif c == '(':
                # Push current result and sign
                stack.append(result)
                stack.append(sign)
                
                # Reset for new sub-expression
                result = 0
                sign = 1

            elif c == ')':
                # Complete current number
                result += sign * num
                num = 0
                
                # Pop sign then previous result
                prev_sign = stack.pop()
                prev_result = stack.pop()
                
                # Apply sign and add to previous result
                result = prev_result + prev_sign * result

        return result + sign * num
