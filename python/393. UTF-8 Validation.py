from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        remaining = 0

        for byte in data:
            if remaining == 0:
                # 1-byte character: 0xxxxxxx
                if byte >> 7 == 0:
                    continue

                # 2-byte character: 110xxxxx
                elif byte >> 5 == 0b110:
                    remaining = 1

                # 3-byte character: 1110xxxx
                elif byte >> 4 == 0b1110:
                    remaining = 2

                # 4-byte character: 11110xxx
                elif byte >> 3 == 0b11110:
                    remaining = 3

                else:
                    return False

            else:
                # Continuation byte must start with 10xxxxxx
                if byte >> 6 != 0b10:
                    return False

                remaining -= 1

        return remaining == 0