class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        
        while a > 0 or b > 0 or c > 0:
            # Take the last bits of a, b, c
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1
            
            # If c's bit is 0, both a and b should be 0
            if bit_c == 0:
                flips += bit_a + bit_b
            else:  # bit_c == 1
                if bit_a == 0 and bit_b == 0:
                    flips += 1
            
            # Right shift all numbers to check next bit
            a >>= 1
            b >>= 1
            c >>= 1
        
        return flips
