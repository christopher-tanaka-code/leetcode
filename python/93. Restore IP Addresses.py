from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        result = []

        # Quick pruning:
        # An IP has exactly 4 parts, each part length is 1 to 3
        if n < 4 or n > 12:
            return []

        def is_valid(part: str) -> bool:
            # No leading zeros unless the part is exactly "0"
            if len(part) > 1 and part[0] == '0':
                return False
            # Must be between 0 and 255
            return int(part) <= 255

        def backtrack(start: int, parts: List[str]) -> None:
            # If we already have 4 parts
            if len(parts) == 4:
                # Valid only if we've used all characters
                if start == n:
                    result.append(".".join(parts))
                return

            # Try parts of length 1, 2, or 3
            for length in range(1, 4):
                if start + length > n:
                    break

                part = s[start:start + length]

                if is_valid(part):
                    parts.append(part)
                    backtrack(start + length, parts)
                    parts.pop()

        backtrack(0, [])
        return result