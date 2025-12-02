class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x: int) -> int:
            s = 0
            while x > 0:
                d = x % 10
                s += d * d
                x //= 10
            return s

        # Floyd's cycle detection (tortoise & hare)
        slow = n
        fast = next_num(n)
        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))
        return fast == 1
