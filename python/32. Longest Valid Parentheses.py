class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # stack holds indices; start with a base index before the string
        stack = [-1]
        best = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:  # ch == ')'
                stack.pop()
                if not stack:
                    # no unmatched boundary to anchor lengths -> reset base
                    stack.append(i)
                else:
                    best = max(best, i - stack[-1])

        return best
