class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending with 0 (but not 0 itself)
        # cannot be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverted = 0
        
        # Reverse half of the number
        while x > reverted:
            digit = x % 10
            reverted = reverted * 10 + digit
            x //= 10
        
        # For even length: x == reverted
        # For odd length: x == reverted // 10 (ignore middle digit)
        return x == reverted or x == reverted // 10
