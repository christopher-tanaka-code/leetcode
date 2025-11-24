class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing bracket -> opening bracket
        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        stack = []
        
        for ch in s:
            # If it's a closing bracket
            if ch in matching:
                # If stack is empty, no matching opening bracket
                if not stack:
                    return False
                # Pop last opening and check if it matches
                top = stack.pop()
                if top != matching[ch]:
                    return False
            else:
                # It's an opening bracket
                stack.append(ch)
        
        # Valid only if no unmatched opening brackets remain
        return len(stack) == 0
