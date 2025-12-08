class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ''

        for char in s:
            if char.isdigit():
                # build the current number (may have multiple digits)
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # push the current string and number onto the stack
                stack.append((current_str, current_num))
                current_str = ''
                current_num = 0
            elif char == ']':
                # pop from stack and build the new string
                prev_str, num = stack.pop()
                current_str = prev_str + current_str * num
            else:
                # normal characters
                current_str += char
        
        return current_str
