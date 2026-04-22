class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {ch: i for i, ch in enumerate(s)}
        stack = []
        in_stack = set()

        for i, ch in enumerate(s):
            if ch in in_stack:
                continue

            while stack and ch < stack[-1] and last_index[stack[-1]] > i:
                in_stack.remove(stack.pop())

            stack.append(ch)
            in_stack.add(ch)

        return "".join(stack)