class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        write = 0  # Pointer to write position
        read = 0   # Pointer to read position

        while read < n:
            char = chars[read]  # Current character
            count = 0

            # Count the number of occurrences of the current character
            while read < n and chars[read] == char:
                read += 1
                count += 1

            # Write the character
            chars[write] = char
            write += 1

            # If count > 1, write its digits
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write
